import random

class markov_model:
	def _init_(self):
		self.objects = []
		self.last_object = object()
		self.last_generated_object = object()
	def add(self, obj):
		if(obj in self.objects):
			count = self.last_object.next.get(obj)
			if(count == None):
				upd = {obj: 1}
			else:
				upd = {obj: count +1}
			self.last_object.next.update(upd)
		elif(len(self.objects) != 0):
			upd = {obj: 1}
			self.last_object.next.update(upd)
			self.objects.append(obj)
		else:
			self.objects.append(obj)
		self.last_object = obj
		
	def generate_next_object(self):
		sum = 0
		for _, count in  self.last_generated_object.next.items():
			sum+=count
		r = random.randint(1,sum)
		for obj, count in self.last_generated_object.next.items():
			r-=count
			if(r<=0):
				self.last_generated_object = obj
				return self.last_generated_object
		return None
		
	def set_start_generate(self, start_with):
		self.last_generated_object = start_with
		
class object:
	def _init_(self, data):
		self.data = data
		self.next = dict()
		
class markov_model_api:
	def _init_(self):
		self.model = markov_model()
		self.model._init_()
		
	def add(self, data):
		obj = object()
		for i in range (0, len(self.model.objects)):
			if(data == self.model.objects[i].data):
				self.model.add(self.model.objects[i])
				return
		obj._init_(data)
		self.model.add(obj)
		
	def put_start(self, start):
		for i in range(0, len(self.model.objects)):
			if start == self.model.objects[i].data:
				start = self.model.objects[i]
				return self.model.set_start_generate(start)
				
	def get(self):
		return self.model.generate_next_object()
		
		
	
