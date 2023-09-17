class ParserEngine:
    @staticmethod
    def extract_args(args):
        data = {}
        for arg in args:
            key, value = arg.split("=")
            if value[0] == '"' and value[-1] == '"':
                value = value[1:-1]
                data[key] = value
            elif value.isdigit():
                value = int(value)
                data[key] = value
            else:
                try:
                    value = float(value)
                    data[key] = value
                except ValueError:
                    continue
        return data

    @staticmethod
    def parse_create(args: str):
        data = {
            "class_name": None,
            "args": None
        }
        if not data:
            raise ValueError("Create command must have A Args <<Class name> <param 1> <param 2> <param 3>")

        data_split = args.split(" ")
        if len(data_split) < 2:
            raise ValueError("Create command must have A Args <Class name> <param 1>")

        data["class_name"] = data_split[0]
        data["args"] = ParserEngine.extract_args(data_split[1:])

        return data


data = "BaseModel name=\"MARIO\" price=15.5 age=10 kingOfBin=True"
ParserEngine.parse_create(data)
