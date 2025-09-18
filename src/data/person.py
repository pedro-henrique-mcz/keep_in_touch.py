'''This module is to hold the person class only'''
import datetime

class Person():
    '''Person class'''
    def __init__(self, name:str, date:datetime.date):
        '''Person class construct'''

        self._valid_args(name, 'name', str)
        self._valid_args(date, 'datetime.date', datetime.date)
        
        self._name = name
        self._date = date
    
    def name(self, name=None) -> str:
        '''Person name handler'''
        if name:
            self._valid_args(name, 'name', str)
            self._name = name

        return self._name

    def date(self, date=None) -> datetime.date:
        '''Person date handler'''
        if date:
            self._valid_args(date, 'datetime.date', datetime.date)
            self._date = date
        
        return self._date
    
    def _valid_args(self, argument_value, arguement_type, valid_type)-> bool:
        '''Tests if the argment of one of our methods 
        are valid, if its not, a error will be raise'''
        
        # if not isinstance(argument_value, valid_type) or not argument_value:
        #     raise ValueError(f'The {arguement_type} must be a {valid_type} type.')
        # else:
        #     return True

        '''Tests if the argment of one of our methods
    are valid, if its not, a error will be raise'''

    # --- ADICIONE ESTA LINHA PARA DEBUG ---
        print(f"\n[DEBUG] Valor='{argument_value}', Tipo='{type(argument_value)}', Condição_do_if='{not isinstance(argument_value, valid_type) or not argument_value}'")
    # ----------------------------------------

        if not isinstance(argument_value, valid_type) or not argument_value:
            raise ValueError(f'The {arguement_type} must be a {valid_type} type.')
        else:
            return True


    def __str__(self):
        '''String representation for debugs'''
        return f'name={self._name}, date={self._date}'


