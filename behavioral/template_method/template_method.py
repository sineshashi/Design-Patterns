'''
Template method pattern is used when we need to replicate the same functionality but for different plug-ins. For example, if we need to interact the same thing with different type of systems or classes, we can use it.
'''

import abc

class Template(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def _step1(self):
        ...

    @abc.abstractmethod
    def _step2(self):
        ...

    @abc.abstractmethod
    def _step3(self):
        ...

    @abc.abstractmethod
    def _step4(self):
        ...

    '''make as many steps as the functionality needs.'''

    def template(self):
        self._step1()
        self._step2()
        self._step3()
        self._step4()

class FunctionalityForSystem1(Template):
    def _step1(self):
        ...
    
    def _step2(self):
        ...
    
    def _step3(self):
        ...
    
    def _step4(self):
        ...
    
'''
Similary we can implement the same functionality for different systems and calling template() method will apply the functionality.
'''