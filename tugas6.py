# Import & Setup
from statistics import stdev
import numpy as np
import pandas as pd
np.random.seed(42)

# NumPy – Data & Statistik
array = np.random.randint(1, 25, size=(5, 2))

rata_rata = np.mean(array)
median = np.median(array)
standard_deviasi = np.std(array)
max = np.max(array)
min = np.min(array)

print("Array 5x5:\n", array)
print("Rata-rata:", rata_rata)
print("Median:", median)
print("Standard Deviasi:", standard_deviasi)
print("Nilai Maksimum:", max)
print("Nilai Minimum:", min)

# pandas – DataFrame
header = ['nama', 'nim', 'nilai']
df = pd.DataFrame(columns=header)
print("\nDataFrame:\n", df)
nilai = [80, 90, 50, 20, 95]
df['nilai'] = nilai
print("\nDataFrame dengan nilai:\n", df)

status = []
for n in nilai:
    if n >= 70: 
        status.append('LULUS')
    else:
        status.append('TIDAK LULUS')
df['status'] = status

print("\nDataFrame:\n")
print(df.head())

with open("ringkasan_tugas6.txt", "w") as f:
    f.write(f"Array 5x5:\n {array}")
    f.write(f"\nRata-rata: {rata_rata}")
    f.write(f"\nMedian: {median}")
    f.write(f"\nStandard Deviasi: {standard_deviasi}")
    f.write(f"\nNilai Maksimum: {max}")
    f.write(f"\nNilai Minimum: {min}")
    f.write(f"\n\nDataFrame:\n {df}")
    
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df
    
    def average(self,) -> float:
        return self.df['nilai'].mean()
    
    def pass_rate(self, threshold: float = 70.0) -> float:
        total = len(self.df)
        passed = len(self.df[self.df['nilai'] >= threshold])
        return (passed / total) * 100 if total > 0 else 0.0

    def save_summary(self, path: str):
        with open(path, "w") as f:
            f.write("=== RINGKASAN NUMPY ===\n")
            f.write(f"Rata-rata: {rata_rata}\n")
            f.write(f"Median: {median}\n")
            f.write(f"Standar Deviasi: {stdev}\n")
            f.write(f"Nilai Minimum: {min}\n")
            f.write(f"Nilai Maksimum: {max}\n\n")

            f.write("=== PANDAS ===\n")
            f.write(f"Jumlah Data: {len(self.df)}\n")
            f.write(f"Nilai Tertinggi: {self.df['nilai'].max()}\n")
            f.write(f"Nilai Terendah: {self.df['nilai'].min()}\n\n")

            f.write("=== OOP: GRADEBOOK ===\n")
            f.write(f"Average Nilai: {self.average()}\n")
            f.write(f"Pass Rate: {self.pass_rate()}%\n\n")
            

if __name__ == "__main__":
    gradebook = GradeBook(df)
    gradebook.save_summary("grade_summary.txt")    