import numpy as np

def calculate_statistics(data):

    arithmetic_mean = np.mean(data)
    

    geometric_mean = np.exp(np.mean(np.log(np.abs(data[data != 0]))))
    

    harmonic_mean = len(data) / np.sum(1.0 / data[data != 0])
    

    median = np.median(data)
    

    variance = np.var(data, ddof=1)  
    
    # محاسبه انحراف معیار
    std_deviation = np.std(data, ddof=1)  
    
    return {
        'arithmetic_mean': arithmetic_mean,
        'geometric_mean': geometric_mean,
        'harmonic_mean': harmonic_mean,
        'median': median,
        'variance': variance,
        'std_deviation': std_deviation
    }

Data1 = [0, -1, 3, 4, 3, 4, 0, 5, 8, 9, -4, 0, 4, 5]
Data2 = [456.7, 547.8, 926.6, 236.1, 543, 439]

stats_data1 = calculate_statistics(Data1)
stats_data2 = calculate_statistics(Data2)

print("Data1 statistics:", stats_data1)
print("Data2 statistics:", stats_data2)