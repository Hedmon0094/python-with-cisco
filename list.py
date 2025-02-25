#lists
#list is a collection of items in a particular order
#list is mutable
#list is defined by square brackets

#creating a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
#output: ['trek', 'cannondale', 'redline', 'specialized']
#accessing elements in a list
print(bicycles[0])
#output: trek
print(bicycles[0].title())
#output: Trek
#accessing the last element in a list
print(bicycles[-1])
#output: specialized
#using individual values from a list
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
#output: My first bicycle was a Trek.
#modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#output: ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)
#output: ['ducati', 'yamaha', 'suzuki']
#adding elements to a list
motorcycles.append('ducati')
print(motorcycles)
#output: ['ducati', 'yamaha', 'suzuki', 'ducati
#inserting elements into a list
motorcycles.insert(0, 'ducati')
print(motorcycles)
#output: ['ducati', 'ducati', 'yamaha', 'suzuki', 'ducati']
