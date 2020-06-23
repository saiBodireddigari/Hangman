def what_to_do(instructions):
    if "Simon says" in instructions:
        if instructions.startswith("Simon says "):
            str_ins = "I" + instructions.replace("Simon says", "")
            return str(str_ins.strip())
        if instructions.endswith(" Simon says"):
            str_ins = "I " + instructions.replace(" Simon says", "")
            return str(str_ins.strip())
        return "I won't do it!"
    return str("I won't do it!")
