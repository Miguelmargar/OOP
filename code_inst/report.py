
class Report():
    #the init is called a constructor
    def __init__(self, message):
        self.message = message
    
    def output(self):
        print(self.message)
        
    def output_upper(self):
        print(self.message.upper())
        
        
class Counter():
    
    def __init__(self, count = 0):
        self.count = count
        
    def increment(self):
        self.count += 1
        
    def decrement(self):
        self.count -= 1
        
    def reset(self):
        self.count = 0
        
    def show(self):
        print(self.count)
        
class Page():
    
    def __init__(self, template, data):
        self.message = template
        self.data = data
    
    def render(self):
        output_text = self.template
        for k, v in self.data.items():
            change_this = "#" + k + "#"
            output_text=output_text.replace(change_this, v)
        return output_text
    
    def save(self, path):
        with open(path, "w") as f:
            f.write(self.render())
            
class HtmlPage(Page):
    
    def __init__(self, template, data):
        self.tem
    
    def render(self):
        output_text = "<html>"
        output_text += super().render()
        output_text += "</html>"
        return output_text