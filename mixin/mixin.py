import logging

# p1
class PrintInfoMixin:
    def print_info(self):
        name = self.__class__.__name__
        attrs = self.__dict__
        return name, attrs


# p2
class MathOperationsMixin:
    def add(self):
        return self.x + self.y

    
    def subtract(self):
        return self.x - self.y

    
    def multiply(self):
        return self.x * self.y


    def divide(self):
        return self.x / self.y


# p3
class LoggingMixin:
    def log(self, message):
        logging.info(message)


    def log_method_call(self, method_name, **kwargs):
        attributes = ', '.join([f'{key}={value}' for key, value in kwargs.items()])
        log_message = f'Calling {method_name} with attributes: {attributes}'
        self.log_info(log_message)

