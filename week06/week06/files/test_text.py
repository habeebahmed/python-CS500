class CourseFile:
	def __init__(self, filename: str) -> None:
		self.__filename = filename;
		
	def write_courses(self, courses: list[str]) -> None:
		with open(self.__filename, "w") as file:
			for course in courses:
				file.write(course + "\n")    

	def read_courses(self) -> list[str]:
		courses = []
		with open(self.__filename) as file:
			for line in file:
				line = line.replace("\n", "")
				courses.append(line)
		return courses   

	def list_courses(self, courses: list[str]) -> None:
		for i in range(len(courses)):
			print(i+1, courses[i])
		print()
  
	def add_course(self, courses: list[str]) -> None:
		course = input("Course: ")
		courses.append(course)
		self.write_courses(courses)
		print(course + " was added.\n")

	def delete_course(self, courses: list[str]) -> None:
		index = int(input("Item no: "))   
		if index < 1 or index > len(courses):
			print('Invalid course no!')
			return
		course = courses.pop(index - 1)
		self.write_courses(courses)
		print(course + " was deleted.\n")
        
def display_menu() -> None:
	print("The Course List program")
	print()
	print("COMMAND MENU")
	print("L - List all courses")
	print("A - Add a course")
	print("D - Delete a course")
	print("E - Exit program")
	print()
    
def main() -> None:
	file = CourseFile("courses.txt")
	display_menu()
	courses = file.read_courses()
	while True:
		command = input("Command: ")
		command = command.lower()
		if command == "l":
			file.list_courses(courses)
		elif command == "a":
			file.add_course(courses)
		elif command == "d":
			file.delete_course(courses)
		elif command == "e":
			print("Bye!")
			break
		else:
			print("Not a valid command. Please try again.")

if __name__ == "__main__":
	main()
