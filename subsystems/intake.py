#making a class for the robot's intake
#neo motors
from rev import CANSparkMax

class Intake:
    #initializing the intake
    def __init__(self, _intake_top_motor : CANSparkMax, _intake_bot_motor : CANSparkMax):
        #reference for the intake motor
        self.intake_top_motor = _intake_top_motor
        self.intake_bot_motor = _intake_bot_motor

    def intake_spin(self, speed):
        #spins the intake motor
        self.intake_top_motor.set(-speed*.6)
        self.intake_bot_motor.set(-speed*.4)

    def stop(self):
        #stops the intake motors
        self.intake_top_motor.set(0)
        self.intake_bot_motor.set(0)