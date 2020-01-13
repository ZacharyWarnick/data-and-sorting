'''
File: BST_Cipher.py

Description: Encrypts and decrypts messages using a binary tree generated from an encrypting key phrase
'''


class Node (object):
	def __init__ (self, data):
		self.data = data
		self.lchild = None
		self.rchild = None

	def __str__(self):
		if self.lchild is not None or self.rchild is not None:
			return "    " +  str(self.data) + " \n" + str(self.lchild) + " " + str(self.rchild)
		else:
			return str(self.data) #just for testing if tree fills, not really qualatative or readable

class Tree (object):
	def __init__ (self):
		self.root = None

	# insert some data into the tree
	def insert (self, data):

		new_node = Node(data)
		if self.search(data):
			return

		if (self.root == None):
			self.root = new_node

		else:
			current = self.root
			parent = self.root
			while (current != None):
				parent = current

				if (ord(data) < ord(current.data)):
					current = current.lchild
				else:
					current = current.rchild

			if (ord(data) < ord(parent.data)):
				parent.lchild = new_node
			else:
				parent.rchild = new_node

	# search for a node with a given data, returns boolean if present, can stop duplicates
	def search (self, data):
		current = self.root
		while (current is not None) and (current.data != data):
			if (data < current.data):
				current = current.lchild
			else:
				current = current.rchild

		return current != None

	def step_search(self,ch):

		output = ""
		current = self.root

		if not self.search(ch):
			output += ""

		elif ch == self.root.data:
			output +=  "*"

		while (current is not None) and (current.data != ch):
			if (ch < current.data):
				current = current.lchild
				output += "<"
			else:
				current = current.rchild
				output += ">"

		return output #returns the instructions to get to a particular character in the tree

	def in_order_print(root):

		if not root:
			return
		in_order_print(root.lchild)
		print (root.data)
		in_order_print(root.rchild)

	def print_node (self, data):
		current = self.root
		while (current is not None) and (current.data != data):
			if (data < current.data):
				current = current.lchild
			else:
				current = current.rchild

		return current

	def traverse(self,st):
		#print(st)

		current = self.root

		for ch in st:
			if ch == ">" and current is not None:
				current = current.rchild
			elif ch == "<" and current is not None:
				current = current.lchild
			else:
				return ""

		try:
			return current.data
		except AttributeError:
			return ""

	def encrypt(self,st):

		output = ""
		for n in st:

			output += self.step_search(n)
			output += "!"
		
		output = output[:-1]

		return output

	def decrypt(self,st):
		
		output = ""
		temp = ""
		current = self.root
		temp = ""

		for ch in (st):
			if ch == "*":   #Add root and look for new instruction
				temp = ""
				continue

			elif ch == "!": #Indicates a new set of instructions to follow, so preint the last set's character and go on
				output += self.traverse(temp)
				temp = ""
				continue

			elif ch == ">" or ch == "<":
				temp += ch

		output += self.traverse(temp)





		return(output)


def main():

	print()


	key = str(input("Enter encryption key: "))
	print()
	tree = Tree()


	key = key.lower() #make lowercase and fill tree, method handles all the complicated direcetional and imput management
	for n in key:
		tree.insert(n)

	encryptInput = str(input("Enter string to be encrypted: "))  #encrypt
	encryptInput = encryptInput.lower()
	print("Encrypted string:", tree.encrypt(encryptInput))

	print()

	decryptInput = str(input("Enter string to be decrypted: "))   #decrypt
	decryptInput = decryptInput.lower()
	print("Decrypted string:", tree.decrypt(decryptInput))

	print()



if __name__ == '__main__':
  main()