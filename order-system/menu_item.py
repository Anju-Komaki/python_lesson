#MenuItem

class MenuItem:
	def __init__(self,name,price):
		self.name = name
		self.price = price

	def info(self):
		return self.name + ': ¥' + str(self.price)

	def get_total_price(self,count):
		total_price = self.price * count

		#3点以上の購入で10%引き
		if count >= 3:
			total_price *= 0.9

		#四捨五入:round
		return round(total_price)