import markov_model

import random #(for test of speed)

api = markov_model.markov_model_api()
api._init_()

api.add('___START___')
api.add(1)
api.add(2)
api.add(3)
api.add(2)
api.add(3)
api.add(1)
api.add(2)

api.put_start('___START___')#don't forget it!

for i in range(0,10):
	print(api.get().data)

#new test

print('\n\n\n\n\n\n\n\n')
api._init_()

api.add('start')
for i in range (0, 1000000): #it takes some time!
	api.add(random.randint(0, 10))

print('added!\n\n')
api.put_start('start')
for i in range(0,50):
	print(api.get().data)
