#print ("What's your name? ")
#name = $stdin.gets()
#puts("Hello, #{name}")
#gets()

module MyModule
	module ClassMethods
		def askQuestion
			puts "What's your name?\n"
		end
	end
end

class MyClass
	include MyModule
	include ClassMethods

	def sayHello(name)
		puts "Hello, #{name.chomp}."
	end
end

ob = MyClass.new

ob.askQuestion

name = gets()

ob.sayHello name

gets()