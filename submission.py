# Part 2
# 1. HMM load
from HMM import HMM
from alarm import alarm_infer
from carnet import car_infer

# model = HMM()
# model.load('two_english')
# print(model.transitions)

# 2. HMM generate
# model = HMM()
# model.load('two_english')
# model.generate(20)

# 3. HMM forward
# model = HMM()
# model.load('two_english')
# observations = model.generate(20)
# print(observations)
# probs = model.forward(observations)
# max_state = max(probs, key=probs.get)
# print(max_state)

# 4. HMM viterbi
model = HMM()
model.load('two_english')
observations = model.generate(20)
print(observations)
probs = model.viterbi(observations)
print(probs)


# Ques 3.1

# mary_given_john = alarm_infer.query(variables=["MaryCalls"], evidence={"JohnCalls": "yes"})
# print(mary_given_john)
#
# john_and_mary_given_alarm = alarm_infer.query(variables=["JohnCalls", "MaryCalls"], evidence={"Alarm": "yes"})
# print(john_and_mary_given_alarm)
#
# alarm_given_mary = alarm_infer.query(variables=["Alarm"], evidence={"MaryCalls": "yes"})
# print(alarm_given_mary)


##########
# Ques 3.2

# result = car_infer.query(variables=["Battery"], evidence={"Moves": "no"})

# Extract the probability of "Battery = Doesn't work"
# probability_battery_doesnt_work = result.values[1]  # Assuming that "Doesn't work" is the second state
# print("Probability that the battery is not working given the car will not move:", probability_battery_doesnt_work)
#
#
# result = car_infer.query(variables=["Starts"], evidence={"Radio": "Doesn't turn on"})
# # Extract the probability of "Starts = no"
# probability_starts_no = result.values[1]  # Assuming that "no" is the second state
# print("Probability that the car will not start given that the radio is not working:", probability_starts_no)


# result_battery_works = car_infer.query(variables=["Radio"], evidence={"Battery": "Works"})
# # Calculate the probability of the radio working when the battery is working and there's gas in the car
# result_battery_works_gas_full = car_infer.query(variables=["Radio"], evidence={"Battery": "Works", "Gas": "Full"})
# # Extract the probabilities of "Radio = turns on" from the results
#
# probability_radio_works_battery_works = result_battery_works.values[0]  # Assuming "turns on" is the first state
# probability_radio_works_battery_works_gas_full = result_battery_works_gas_full.values[0]  # Assuming "turns on" is the first state
#
# print("Probability of the radio working when the battery is working:", probability_radio_works_battery_works)
# print("Probability of the radio working when the battery is working and there's gas in the car:", probability_radio_works_battery_works_gas_full)
# print("NO IT DOESNT CHANGES, TY THE SAME")


# # Calculate the probability of the ignition not working when the car doesn't move
# result_moves_no = car_infer.query(variables=["Ignition"], evidence={"Moves": "no"})
# # Calculate the probability of the ignition not working when the car doesn't move and there's no gas in the car
# result_moves_no_gas_empty = car_infer.query(variables=["Ignition"], evidence={"Moves": "no", "Gas": "Empty"})
# # Extract the probabilities of "Ignition = Doesn't work" from the results
# probability_ignition_doesnt_work_moves_no = result_moves_no.values[1]  # Assuming "Doesn't work" is the second state
# probability_ignition_doesnt_work_moves_no_gas_empty = result_moves_no_gas_empty.values[1]  # Assuming "Doesn't work" is the second state
#
# print("Probability of the ignition not working when the car doesn't move:", probability_ignition_doesnt_work_moves_no)
# print("Probability of the ignition not working when the car doesn't move and there's no gas in the car:", probability_ignition_doesnt_work_moves_no_gas_empty)
# print("the probability reduces when there is no gas in the car")



# probability_starts_yes_radio_and_gas = car_infer.query(variables=["Starts"],evidence={"Radio": "turns on", "Gas": "Full"})
# print("Probability that the car starts if the radio works and has gas:", probability_starts_yes_radio_and_gas.values[0])


############
# Q 3.3

# print(car_infer.query(variables=['KeyPresent'], evidence={}))
# print(car_infer.query(variables=['KeyPresent'], evidence={'Starts': 'yes'}))
# print(car_infer.query(variables=['KeyPresent'], evidence={'Starts': 'no'}))

