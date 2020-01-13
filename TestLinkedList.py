'''
File: TestLinkedList.py

Description: Linked list testing functions
'''

class Link (object):
	def __init__ (self, data, next = None):
		self.data = data
		self.next = next

class LinkedList (object):
	def __init__ (self):
		self.first = None

	def __str__(self):

		outList = ""
		current = self.first
		count = 0
		while current != None:
			count += 1
			if count <= 10:
				outList += (str(current.data)) + "  "
				current = current.next
			else:
				outList += str(current.data) + "\n"
				count = 0
				current = current.next



		return outList

	def get_num_links(self):
		current = self.first
		count = 1
		while current.next != None:
			count += 1
			current = current.next

		return count

	def insert_first (self, data):
		new_link = Link (data)

		new_link.next = self.first
		self.first = new_link

	def insert_last (self, data):
		new_link = Link (data)

		current = self.first
		if (current == None):
			self.first = new_link
			return

		while (current.next != None):
			current = current.next

		current.next = new_link

	def insert_in_order(self,data):
		return

	def sort_list(self):

		newLinkedList = LinkedList()
		current = self.first
		data = []
		while current.next != None:
			data.append(current.data)
			current = current.next

		data.append(current.data)
		data.sort()

		for elt in data:
			newLinkedList.insert_last(elt)

		return newLinkedList
		
	def copy_list(self):

		newLinkedList = self
		current = self.first

	
		return newLinkedList

	def reverse_list(self):

		newLinkedList = LinkedList()
		current = self.first
		data = []

		while current.next != None:
			data.append(current.data)
			current = current.next

		data.append(current.data)

		data.reverse()

		for elt in data:
			newLinkedList.insert_last(elt)

		return newLinkedList

	def find_ordered(self,data):

		target = Link(data)
		current = self.first

		while current.next != None:
			if current.data == target.data:
				return True
			current = current.next
		return False

	def find_link (self, data):
		current = self.first

		if (current == None):
			return None

		while (current.data != data):
			if (current.next == None):
				return None
			else:
				current = current.next

		return current

	def is_sorted(self):


		current = self.first
		while current.next != None:

			if current.data > current.next.data:
				
				return False
			current = current.next

		return True

	def delete_link (self, data):
		previous = self.first
		current = self.first

		if (current == None):
			return None

		while (current.data != data):
			if (current.next == None):
				return None
			else:
				previous = current
			current = current.next

		if (current == self.first):
			self.first = self.first.next
		else:
			previous.next = current.next

		return current

	def is_empty(self):

		return self.first == None

	def merge_list(self,other):

		mergedList = LinkedList()

		data = []

		selfCurrent = self.first
		otherCurrent = other.first

		mergedList.insert_first(selfCurrent.data)
		mergedList.insert_first(otherCurrent.data)

		while selfCurrent.next != None:
			data.append(selfCurrent.data)
			selfCurrent = selfCurrent.next

		while otherCurrent.next != None:
			data.append(otherCurrent.data)
			otherCurrent = otherCurrent.next

		data.sort()
		
		for n in data:
			mergedList.insert_first(n)
			print(n)

		return mergedList	

	def remove_duplicates(self):

		newLinkedList = LinkedList()
		current = self.first
		data = []
		while current.next != None:
			data.append(current.data)
			current = current.next

		data.sort()
		data = set(data)
		for elt in data:
			newLinkedList.insert_last(elt)

		return newLinkedList

	def is_equal(self,other):

		selfCurrent = self.first
		otherCurrent =  other.first
		eq = False

		if self.get_num_links() == other.get_num_links():
			while selfCurrent.data == otherCurrent.data and selfCurrent.next != None:
				eq = True
				selfCurrent = selfCurrent.next
				otherCurrent = otherCurrent.next
				if selfCurrent == None and otherCurrent == None:
					eq = True

		return eq
		



def main():
	print()

	links = LinkedList()

	data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
	extra = [9,3,4,1,5,134,151,34,1,144]
	for n in data:

		links.insert_first(n)
	# insert
	print(links)
	links.insert_last(100)
	print()
	print(links)
	print()
	#num links
	print("Num links:",links.get_num_links())
	print()
	# find itme in list
	print("Find ordered:",links.find_ordered(5),links.find_ordered(999))
	print()
	#delete a link
	links.delete_link(100)
	print(links)
	print()

	#copy a list
	copy = links.copy_list()
	print(copy)
	print()

	#reverse
	reverseList = links.reverse_list()
	print(reverseList)
	print()

	#sort the list
	sortedList = links.sort_list()
	print(sortedList)
	print()

	#return if it is already sorted
	print("Is sorted:",links.is_sorted())
	print()

	#return if it is empty
	empty = LinkedList()
	print("Is empty:",links.is_empty(),empty.is_empty())
	print()

	l1 = LinkedList()
	l2 = LinkedList()
	l1.insert_first(1)
	l2.insert_first(5)

	#merge two lists
	mergedList = (l1.merge_list(l2))
	print(mergedList)

	eq1 = LinkedList()
	eq2 = LinkedList()
	eq1.insert_first(1)
	eq2.insert_first(2)

	#retunr in two lists are equal
	print()
	print(links.is_equal(links),eq1.is_equal(eq2))
	print()

	#remove duplicates
	dupTest = LinkedList()
	for n in range(25):
		dupTest.insert_first(1)

	print(dupTest)
	print()

	dupTest = dupTest.remove_duplicates()
	print(dupTest)


if __name__ == "__main__":
  main()