#!/usr/bin/python
from os.path import abspath, dirname, basename, sep, exists
import re
from xml.etree import ElementTree as ET


REGEX_MAGENTO_QUALIFIED_NAME = re.compile(r'(?P<namespace>[a-zA-Z0-9]+)_(?P<module>[a-zA-Z0-9]+)(?P<pclass>(?:_(?P<classname>[a-zA-Z0-9]+))+)?')

output = ''
package_dir=''
module_dir=''

declared_modules = []
modules = {} # keyed by members in declared_modules list

class Component:
	def __init__(self, namespace=None, name=None):
		self.namespace = namespace
		self.name = name
		self.errors = []
		
	def add_error(self, error_message, line=None):
		if line == None:
			self.errors.append(error_message)
		elif len(line)>=2:
			self.errors.append(error_message + ' at %s:%s' % line[0:2])
		elif len(line)==1:
			self.errors.append(error_message + ' at %s' % line[0])
	
	@property
	def is_verified(self):
		return len(self.errors)==0

class Module(Component):
	def __init__(self, namespace=None, name=None):
		Component.__init__(self, namespace, name)
		
		self.models = {}
		self.blocks = {}
		self.helpers = {}
		self.resources = {}

	def add_error(self, component_type, name, error_message, line=None):
		'''
		@param component: Either module, model, block, helper or resource
		@param name: Name of the component
		@param line: a tuple of config line and line number
		'''
		# Resolve to the correct error stack
		errors = None
		if component_type in ['model', 'block', 'helper', 'resource']:
			error_regs = None
			if component_type == 'model':
				error_regs = self.models
			elif component_type == 'block':
				error_regs = self.blocks
			elif component_type == 'helper':
				error_regs = self.helpers
			elif component_type == 'resource':
				error_regs = self.resources
			if not name in error_regs:
			# new list if not already in the list
				error_regs[name] = Component((self.namespace, self.name), name)
			component = error_regs[name]
			component.add_error(error_message, line)
		elif component_type == 'module':
			Component.add_error(self, error_message, line)

def banner():
	print 'WELCOME TO MAGENTO MODULE VALIDATOR'

def limited_choices(choices, case_sensitive=False):
	'''
	usage: 
	@limited_choices(['y','n'])
	def prompt_for_something():		
	'''
	if len(choices)==0:
		raise Error('Please specify the choices OR remove the annotation!')
	if not case_sensitive:
		# generate a new list of all lower case letters
		choices = [item.lower() for item in choices]

	def wrapper(target):
		print "Modifying TARGET's behavior"
		def wrapped():
			while True:
				result = target()
				if not case_sensitive:
					result = result.lower()
				if result in choices:
					return result
				else:
					print 'Please choose from ',choices	
		return wrapped
	return wrapper

def verify_wellform(file):
	try:
		ET.parse(file)
		return True
	except:
		print 'Config file %s is not well-formed' % file.name        
		print 'Please double check'
		return False

def validate(config_file):
	'''
	@type config_file: File object
	'''
	print 'Please wait, the process may take a few minutes'
	print 'Analyzing... '
	root = ET.parse(config_file).getroot()
	modules_node = root.find('modules')
	global_node = root.find('global')

	for module_config in modules_node:
		# Iterate node config/modules and pick up the modules
		# variable modules is referred to at global scope by validate_X methods
		module_name = module_config.tag.lower()
		declared_modules.append(module_name)
		module = validate_module(module_config)
		modules[module_name] = module

	model_config = global_node.find('models')
	validate_model(model_config)

	block_config = global_node.find('blocks')
	validate_block(block_config)

	helper_config = global_node.find('helpers')
	validate_helper(helper_config)

	resource_config = global_node.find('resources')
	validate_resource(resource_config)

	return True

def validate_module(module_config):
	tag = module_config.tag
	match = REGEX_MAGENTO_QUALIFIED_NAME.match(tag)
	
	module = Module()
	if match == None:
		# Return an empty module
		module.add_error('module',None,'Invalid Namespace_Modulename format')
	elif len(match.groups())>=2:
		module.namespace = match.group('namespace')
		module.name = match.group('module') 
	else:
		module.add_error('module',None,'Namespace_Modulename missing')
	return module

def validate_component(component_config, component_type):
	'''
	@param context: model, block, helper, resource 
	'''
	for module_config in component_config:
		if module_config.tag in declared_modules:
			module = modules[module_config.tag]
			classname = module_config.find('class').text
			n_m_c = validate_classname(classname, 'N_M_C') 
			if type(n_m_c) is tuple:
				errors = validate_classfile(n_m_c)
				if errors == True:
					pass
				else:	
					for error in errors:
						module.add_error(component_type, classname, error)
			else:
				for error in n_m_c:
					module.add_error(component_type, classname, error)
		else:
			pass # Config level error

def validate_model(model_config):
	validate_component(model_config, 'model')

def validate_block(block_config):
	validate_component(block_config, 'block')
	
def validate_helper(helper_config):
	validate_component(helper_config, 'helper')

def validate_resource(resource_config):
	validate_component(resource_config, 'resource')

# Validate physical assets of the components

def validate_classname(classname, required='N_M_C'):
	match = REGEX_MAGENTO_QUALIFIED_NAME.match(classname)
	errors = []
	if match == None:
		errors.append('Invalid Namespace_Modulename_Package_Classname format')
		return errors
	else:
		if required=='N_M_C':
			if match.group('namespace') == None:
				errors.append('Namespace is missing')
			if match.group('module') == None:
				errors.append('Module is missing')
			if match.group('pclass') == None:
				errors.append('Package_Class is missing')
			
			if len(errors)==0:
				return (match.group('namespace'), match.group('module'), match.group('pclass')[1:])
			else:
				return errors
		elif required=='N_M':
			if match.group('namespace') == None:
				errors.append('Namespace is missing')
			if match.group('module') == None:
				errors.append('Module is missing')
			
			if len(errors)==0:
				return (match.group('namespace'), match.group('module'))
			else:
				return errors
		else:
			raise Error('Invalid required specification')

def validate_classfile(class_info):
	if len(class_info)==3:
		file_path = sep.join([item for item in class_info[2].split('_') if len(item)>0])  + '.php'
		file_path = sep.join([package_dir,module_dir,file_path])
		if exists(file_path):
			return True
		else:
			return ['%s does not exist' % file_path]
	elif len(class_info)==2:
		return ['%s/%s is not a valid file' % class_info]

@limited_choices(['Y','n'])
def confirm_report():
	return raw_input('Would you like to save this report? (Y/n) ')

def report():
	print 'Reporting...\n===================================='
	print 'Modules:'
	for module in declared_modules:
		print '- ', module
	
	print 'Module details:'
	for module in modules.values():	
		print '- ', module.name
		print '\t''+Models:'
		for name, component in module.models.items():
			if component.is_verified:
				print '\t'*2,'%s: OK' % name
			elif len(component.errors)==1:
				print '\t'*2,'%s: %s' % (name, component.errors[0])
			else:
				print '\t'*2,'%s:' % name
				for error in component.errors:
					print '\t>'*3, error
		print '\t''+Blocks:'
		for name, component in module.blocks.items():
			if component.is_verified:
				print '\t'*2,'%s: OK' % name
			elif len(component.errors)==1:
				print '\t'*2,'%s: %s' % (name, component.errors[0])
			else:
				print '\t'*2,'%s:' % name
				for error in component.errors:
					print '\t>'*3, error	
		print '\t''+Helpers:'
		for name, component in module.helpers.items():
			if component.is_verified:
				print '\t'*2,'%s: OK' % name
			elif len(component.errors)==1:
				print '\t'*2,'%s: %s' % (name, component.errors[0])
			else:
				print '\t'*2,'%s:' % name
				for error in component.errors:
					print '\t>'*3, error
		print '\t''+Resources:'
		for name, component in module.resources.items():
			if component.is_verified:
				print '\t'*2,'%s: OK' % name
			elif len(component.errors)==1:
				print '\t'*2,'%s: %s' % (name, component.errors[0])
			else:
				print '\t'*2,'%s:' % name
				for error in component.errors:
					print '\t>'*3, error
#	choice = limited_choices(['Y','n'])(lambda:raw_input('Would you like to save this report? (Y/n)'))()
	choice = confirm_report()
	if choice == 'y':
		path = raw_input('File location:')
		try:
			with open(path,'w') as f:
				# Context manager will close the file f for us
				f.write(output)
		except IOError as (errno, errstr):
			print 'Error %d: %s' % (errno, errstr)
	print 'CHOICE: ',choice

def prompt_for_config_xml():
	print 'Please specify a Magento module config file'
	while True:
		path = raw_input('File location:')
		try:
			with open(path) as f:
				# Context manager will close the file f for us
				if verify_wellform(f):
					return path
		except IOError as (errno, errstr):
			print 'Error %d: %s' % (errno, errstr)

def main():
	global package_dir, module_dir
	
	banner()
	while True:	
		path = prompt_for_config_xml();
		# Path must satisfy the precondition of:
		# 1. Accessible
		# 2. Well-formed
		module_dir = dirname(dirname(abspath(path))) # Up two levels
		package_dir = dirname(module_dir)
		module_dir = basename(module_dir) # Take the directory name only
		
		validate(path)
		report()

if __name__ == '__main__':
	main()
