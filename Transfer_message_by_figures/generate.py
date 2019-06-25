import os
import math
import random
import shutil

alphabet_path = r'alphabet'
target_path = r'Test'
# Generate dictionary
def generate_dict(path):
	''' Generate Picture Dictionary
	:params path: alphabet pictures dir path
	:return alphabet_dict: {'A' : 'athens',...}
	'''
	origin_path = os.getcwd()
	os.chdir(path)
	values = sorted([f[:-4] for f in os.listdir(path) if f.endswith('.jpg')])
	keys = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ. ')
	alphabet_dict = dict(zip(keys, values))
	os.chdir(origin_path)
	return alphabet_dict

# Generate Rename list
def generate_rename(s, alpha_dict):
	''' Generate a rename list for the given string seek
	:params s: Input UpperCase string
	:params alpha_dict: Alphabet Picture Filename
	:params new: File name list according to s
	'''
	N = len(s)
	all_az = 'abcdefghijklmnopqrstuvwxyz'
	candidates = [a+b+c for a in all_az for b in all_az for c in all_az]
	old = [alpha_dict[si] for si in s]
	add_new = sorted([random.choice(candidates) for i in range(N)])
	new = [a+b for (a,b) in zip(add_new, old)]
	return new
	

# Generate a series of pictures of right order
def generate_pic_dir(s, alpha_dict, start_path, end_path):
	''' Generate pictures in order to some directory
	:params s: Input UpperCase string
	:params alpha_dict: Alphabet Picture Filename
	:params start_path: Pictures origin path
	:params end_path: Generate Picture Path
	'''
	f_old_list = [alpha_dict[si] for si in s]
	f_new_list = generate_rename(s, alpha_dict)
	for (f_old, f_new) in zip(f_old_list, f_new_list):
		shutil.copy(os.path.join(start_path,f_old+'.jpg'), end_path)
		os.rename(
					os.path.join(end_path,f_old+'.jpg'), 
					os.path.join(end_path,f_new+'.jpg'))

# Encode filename by add nums
def encode_f_names(path):
	''' Encode filenames by inserting random numbers
	'''
	for f in os.listdir(path):
		f_name, ext = os.path.splitext(f)
		rd = random.randint(0, 5)
		nums = '0123456789'
		tmp = list(f_name)
		for i in range(rd):
			idx = random.randint(0, len(tmp)-1)
			tmp.insert(idx, random.choice(nums))
		f_new_name = ''.join(tmp)
		os.rename(
					os.path.join(path,f_name+'.jpg'), 
					os.path.join(path,f_new_name+'.jpg'))

# Decode filename by strip nums
def decode_f_names(path):
	''' Decode filenames by removing random numbers
	'''
	for f in os.listdir(path):
		f_old = f
		print('Old File Name: %s' % f_old)
		remove_digits = str.maketrans('', '', '0123456789')
		f_new = f_old.translate(remove_digits)
		print('New File Name: %s' % f_new)
		os.rename(os.path.join(path,f_old), os.path.join(path,f_new))

if __name__ == '__main__':
	alphabet_path = os.path.join(os.getcwd(), alphabet_path)
	target_path = os.path.join(os.getcwd(), target_path)
	
	az_dict = generate_dict(alphabet_path)
	s = input("Input some sentences: \n").upper()
	flag = eval(input('Encode[0]/Decode[1]: '))
	if not flag:
		generate_pic_dir(s, az_dict, alphabet_path, target_path)
		encode_f_names(target_path)
	else:
		decode_f_names(target_path)