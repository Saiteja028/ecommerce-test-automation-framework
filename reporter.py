from datetime import datetime

class Reporter:
    def __init__(self):
        self.results= []
        self.current = None

    def start(self, name):
        self.current = {"name":name, "start":datetime.now, "steps":[]}

    def log(self,step,status="PASS"):
        if(self.current):
            self.current["steps"].append({"step":step, "status":status})

    def end(self,status):
        if self.current:
            self.current["status"]=status
            self.current["end"]=datetime.now()
            self.results.append(self.current)
            self.current=None

    def     summary(self):
        print("\n===Report===")
        for r in self.results:
            print(f"{r['status']:<4} {r['name']} steps={len(r['steps'])}")

reporter = Reporter()
