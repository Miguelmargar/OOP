from report import *

c = Counter()
d = Counter(99)

r = Report("hello world")

r.output()
r.output_upper()
#---------------------------------------------------------
c.increment()
c.increment()
c.decrement()
c.show()

d.increment()
d.show()
#---------------------------------------------------------
people = {
    "dolly": Counter(2),
    "miguel": Counter(2)
}

people["dolly"].increment()
people["dolly"].show()
people["miguel"].show()
#---------------------------------------------------------

person = {
    "name" : "Richard",
    "city" : "Dublin"
}

home = Page("<h1>Hello #name#, the wheather in #city# is:</h1>", person)
print(home.render())
home.data = {"name": "Miguel"}
print(home.render())

home.save("home.html")


