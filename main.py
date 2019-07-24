import textrank
import googlescraper

text = "This section is about abstract classes. Let's consider these examples. These are fairly famous problem. So you had this ship class and then we inherited from the shape class and treat a rectangular class and we'll take one more class. So we inherited the shape class and then create a circle class. So let's have some methods for these as well. So before the methods, we can have some properties obviously for the ship trustee. Can't think of anything but uh, the, we could have a ship constructor, so let's say public share and then maybe we don't do anything or there. But uh, for the rectangle class of course we can think of two dimensions. So let's see. Land and the width. And uh, we are going to also area will defined the area for this. That'll be public int you say cattle carrier. And he's basically, we'll return land into it. And uh, we lost to have a constructor, public rectangle. So we'll have anti land and I interviewed and uh, we can assign this. That's basically how you can do that. Should be returned. I can write the same kind of stuff for the separate class. We take censorship, this is the constructor for that. So there's a property called radius and the area is fire squad. So you can get fired for Matt. Dot. Five a into reducing into radius. Okay, so there's this math.fi which you can use for get the invites to the radius of the radius. You can actually calculate the area so it will be fired. Squared. Uh, we have a problem returning this. Let's actually try to run this and see. Yeah. So the, the problem is like this is actually double. So we'll, we'll do this entire computation and then cry to cost to an indigent. That might be a better kind of arrangement. Let me see whether it works out that should be better and that we don't have any others. Right? So, um, let's also modify the shape class. You can think of an area. This is going to be, um, the, the area of a ship. Um, obviously we don't know how to compute an area of ship. Maybe we'll return zero. All right. So, um, so here we have the best glass rectangle class and a second class. So we can create objects of all three classes that can have a ship class called s. There are no properties for them. Then maybe I can have a rectangle class. Let's say 10 km. A FAPE are the dimensions. I can also have a circuit class. So let's see, the radius is 10 and I am going to display the areas of each one of them. So it's going to be s. Dot. Cattle carrier and a similarly, I can do it for the other ones as well. Here are the key eds for the rectangle and a circle as well. Now let me been this code. So if an underscore, they will get sued over the ship, 50 for the rectangle and 314 for that separate. So that's uh, how it works out. But, um, if you look at this court, um, it's very clear, right? It's very clear that we can't do, we can't define an area for a chip. Let's see. We want to prevent shape classes from being created in the first place. So the part that you want to kind of stop this disbarred, because this doesn't make any sense. There's no sense making actually a shape type objects. So we want this kind of statement to be, uh, to generate an error because it doesn't make any sense at all. So what I can do is I can define this class as an abstract class. And when you define the classes that answer class, one of the main things that happens is, um, you can't create objects of an abstract class. That is a key, um, reason why you might want to use an abstract class. We don't want, um, shape type objects to be created. Now, if you try to compile this code, it will generate and you can't actually see a new shape. So, but you can have a shape type variable, but you are not allowed to do is to create an object. So this part of the code is the one that is not valid. Uh, obviously we'll have a runtime error when we credit cleaned s I think it'll, uh, might give you another. Yeah. So that's because we have not created this object, but I say like as we learned earlier as is actually a circle. So, um, it actually follows relationship. If you have a superclass, you can create subclasses, subclass objects at. So, um, this arrangement is always possible. So chip is a superclass and you can create objects of subclasses of the superclass that is totally allowed. So let me now run the code to all those shape is static. I'd rather ship is abstract, I'll do shape is abstract. Um, you, you can actually have a variable but assign it to a different subclass object. So, uh, that's uh, is basically about, uh, abstract classes in this abstract class called shape. We are trying to do, we are trying to do this calculation of calculate area, but there must be an easy way in a better way of doing this because really zero has no meaning. So we can also have something called abstract methods. So if you have an abstract, but it is what you do and then it just becomes a declaration because you're, you're crying to say that, um, you have this method called Calico area. Um, but if you have an abstract method, your subclasses have to implement them, so your subclasses must implement it, right? So that, that's a real requirement. So, um, so this code will run. You can see that. But, um, but if you have a class called square, right, and you just do this, we'll just extend a ship just for the sake of doing it. And, uh, let, let's just leave it later. So when you do that, so we just created a new class. Uh, what can you see this edit? It says, yeah. Um, that basically you need to have, you have to override this abstract method call calc area. So all the subclasses must override this abstract method. The example of, uh, how abstract classes I use triangle circle, rectangular, solid, normal classes. But the ship class can be an abstract class because it doesn't make any sense to create stereotype objects. So this is what you have in the, in the early example, we, we saw this, but, um, uh, as you saw, uh, if you want to prevent, if you want to prevent, um, ship class objects being created, we can have a abstract class for shape and we can also have an abstract method for, uh, uh, get idiot. So that's basically how abstract classes look. So every, um, subclass, every child class must override or redefine the abstract methods that you have. So, um, that that becomes a requirement. If you have a class that does not override the abstract methods, then debt also has to become abstract, which is a fairly unusual, these are some general observations about abstract classes. You can't treat objects as the key thing. And, um, also if you have a class hierarchy, typically the, the most, uh, based class would be abstract. They very general. And, uh, that's basically how you would, uh, kind of think of it. So in situations where you doing foreign objects to be created, you can have abstract classes and you can also force your sub classes to implement certain and methods by, uh, basically having abstract methods. "

stage1 = list()

for graf in textrank.parse_doc(text):
    stage1.append(textrank.pretty_print(graf._asdict()))

graph, ranks = textrank.text_rank(stage1)
textrank.render_ranks(graph, ranks)

key_phrases = textrank.normalize_key_phrases(stage1, ranks)

keyword = next(key_phrases).text

links = list()

for serp in googlescraper.getUrls(keyword):
    # print(serp)
    for link in serp.links:
        links.append(link.link)

print(links)
