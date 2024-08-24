from car import Car
from customers import Customer
from rental import Rental
#create cars
car1 = Car("C001","toyota","innova",2022)
car2 = Car("C002","honda","accord",2022)
#create customers
Customer1 = Customer('CU001',"nikkita jore")
Customer2 = Customer('CU002',"vivek k")
Customer1.rent_car(car1)
Customer2.rent_car(car2)
print(f"{Customer1.name}'s Rented Cars:{[car.make for car in Customer1.rented_cars]}")
print(f"{Customer2.name}'s Rented Cars:{[car.make for car in Customer2.rented_cars]}")
Customer1.return_car(car1)
print(f"{Customer1.name}'s Updated Rented Cars:{[car.make for car in Customer1.rented_cars]}")
print(f"{Customer2.name}'s  Updated Rented Cars:{[car.make for car in Customer2.rented_cars]}")
#create rental
rental1 = Rental("R001",Customer1,car1,rental_fee=500.0)
rental2 = Rental("R002",Customer1,car2,rental_fee=450.0)
#display rental information
print(f"Rental ID:{rental1.rental_id},Customer:{rental1.customer.name},Car:{rental1.car.make},Rental Fee:INR {rental1.rental_fee}")
print(f"Rental ID:{rental2.rental_id},Customer:{rental2.customer.name},Car:{rental2.car.make},Rental Fee:INR {rental2.rental_fee}")


