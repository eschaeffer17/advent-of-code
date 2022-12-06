from pathlib import Path

def read_daily_input(day, separator='\n'):
    input_path = "../inputs/"+day+".txt"
    path = Path(__file__).parent / input_path

    with path.open() as f:
        data = f.read()
    
    data = data.split(separator)

    return [i for i in data if len(i)!=0]

