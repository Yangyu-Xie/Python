import random
import copy

def present_exchange(group):
	present_holder=copy.copy(group) # bacause when we assign the variabl, it will be passed by reference, so we will need to use copy to pass the obj.
	receiver_group=copy.copy(group)
	received=[]
	conb=[]
	
	for i in range(len(group)):
		sender=random.choice(present_holder)  # this line contorls who hold the present.
		present_holder.remove(sender) 		
		if sender in receiver_group: 
			receiver_group.remove(sender) # remove the sender from the receiver group, but only when the sender is in the list.
		receiver=random.choice(receiver_group) 
		receiver_group.remove(receiver) 
		received.append(receiver)		
		if sender not in received:
			receiver_group.append(sender) #if the sender already got the present, he should not be added back to receiver group/
		conb.append([sender,receiver])
	return conb


print(present_exchange(["Fred","Wilma","Barney","Pebbles","Bam Bam","jackie","chen"]))
