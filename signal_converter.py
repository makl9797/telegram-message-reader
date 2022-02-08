class Signal:
    def __init__(self, asset, ordertype, duration, risk):
        self.asset = asset
        self.ordertype = ordertype
        self.duration = duration
        self.risk = risk

    def __repr__(self):
        return "This is object of class A"

    def __str__(self):
        output = "{asset: %s, ordertype: %s, duration: %s, risk: %s" % (
            self.asset, self.ordertype, self.duration, self.risk)
        output += "}"

        return output

# extract functions needs optimization (bad practice)


def extract_asset(msg):
    start = msg.find("$") + 1
    end = msg.find("USDT")
    return msg[start:end]


def extract_ordertype(msg):
    if msg.find("closed") == -1 and msg.find("New signal") != -1:
        return "BUY"
    elif msg.find("New signal") == -1 and msg.find("closed") != -1:
        return "SELL"
    else:
        return None


def extract_duration(msg):
    if msg.find("Type:") != -1:
        start = msg.find("Type: ")+6
        end = msg.find(" - Risk:")
        return msg[start:end]
    else:
        None


def extract_risk(msg):
    if msg.find("Risk: ") != -1:
        start = msg.find("Risk: ")+6
        end = msg.find(")")
        return msg[start:end]
    else:
        None


def msg_to_signal(msg):
    return Signal(extract_asset(msg), extract_ordertype(msg),
                  extract_duration(msg), extract_risk(msg))
