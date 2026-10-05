students=int(input("enter the students:"))
each_bench_students=3
total_benches=students//each_bench_students
remaining_students=students%each_bench_students
print(f"total_benches:{total_benches},remaining_students:{remaining_students}")