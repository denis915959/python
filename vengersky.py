# python vengersky.txt
import copy

A1=[[32.0, 28.0, 4.0, 26.0, 4.0], [17.0, 19.0, 4.0, 17.0, 4.0], [4.0, 4.0, 5.0, 4.0, 4.0], [17.0, 14.0, 4.0, 14.0, 4.0], [21.0, 16.0, 4.0, 13.0, 4.0]] #res=39
#A1=[[2.0, 5.0, 3.0, 10.0, 4.0], [6.0, 4.0, 8.0, 1.0, 1.0], [4.0, 6.0, 5.0, 3.0, 5.0], [3.0, 2.0, 6.0, 4.0, 3.0], [3.0, 1.0, 1.0, 4.0, 4.0]] #res = 9
#A1=[[3.0, 7.0, 4.0, 11.0, 8.0], [7.0, 6.0, 9.0, 2.0, 5.0], [4.0, 8.0, 6.0, 6.0, 9.0], [2.0, 7.0, 6.0, 4.0, 5.0], [4.0, 3.0, 2.0, 5.0, 8.0]] #res=18

class mesh():
	def __init__(self, x1, y1):
		self.string=x1  #номер строки
		self.column=y1  #номер столбца

def min_null(arr): #игнорит нули
	min=10000000000
	n = len(arr)
	for i in range(0, n):
		if(arr[i]!=0)and(arr[i]<min):
			min=arr[i]
	return min

def vengersky_algoritm(A):
	n=len(A[0])
	M=copy.deepcopy(A) #так как матрицу A мы портим
	pp=0
	null_arr=[]
	while(len(null_arr)!=n):
		null_arr.clear()
		pp=pp+1
		#первый пункт, вычитание минимума из строки
		for i in range(0, n):
			min_str=min(A[i])
			for j in range(0, n):
				A[i][j]=A[i][j]-min_str

		for j in range(0, n): #если в каких-то столбцах нет нулей, то они там появятся (по аналогии со строкой)
			flag=False
			for i in range(0, n):
				if(A[i][j]==0):
					flag=True
			if(flag==False):
				column=[]
				for k in range(0, n):
					column.append(A[k][j])
				min_str=min(column)
				for i in range(0, n):
					A[i][j]=A[i][j]-min_str
				column.clear()

		#второй пункт
		null_count=[]
		for i in range(0, n):
			count=0
			for j in range(0, n):
				if(A[i][j]==0):
					count=count+1
			null_count.append(count)

		zero_in_A=True
		A_temp=copy.deepcopy(A) #рекурсивный метод
		num_zero_string=[] #массив номеров вычеркнутых строк
		num_zero_column=[] #массив номеров вычеркнутых столбцов

		while(zero_in_A): #вычеркиваем строки и столбцы из матрицы, убирая все нули (заполняем -1)
			null_count=[] #сначала смотрим строки
			for i in range (0, n): #ищем число нулей в каждой строке
				count=0
				for j in range(0, n):
					if(A_temp[i][j]==0):
						count=count+1
				null_count.append(count)
			for j in range (0, n): #ищем число нулей в каждом столбце
				count=0
				for i in range(0, n):
					if(A_temp[i][j]==0):
						count=count+1
				null_count.append(count)
			max_zero=max(null_count)#находим max ЧИСЛО нулей
			num_max=-1
			for i in range(0, 2*n):
				if(null_count[i]==max_zero):
					num_max=i
					break
			#куда-то сюда вставить еще одну проверку
			if(num_max<n): #в строке с max числом нулей все элементы делаем =-1
				if(null_count[num_max]==1):
					#находим номер столбца, в котором содержится этот ноль
					col_num=-1
					for i in range(0, n):
						if(A_temp[num_max][i]==0.0):
							col_num=i
							break
					#находим число -1 в столбце
					col_count=0
					for i in range(0, n):
						if(A_temp[i][col_num]==-1):
							col_count=col_count+1
					#находим число -1 в строке
					str_count=0
					for j in range(0, n):
						if(A_temp[num_max][j]==-1):
							str_count=str_count+1
					if(str_count > col_count):   #вычеркиваем строку
						for j in range(0, n):
							A_temp[num_max][j]=-1
						num_zero_string.append(num_max)
					else:   #вычеркиваем столбец
						for i in range(0, n):
							A_temp[i][col_num]=-1
						num_zero_column.append(col_num)

				else:
					num_zero_string.append(num_max)
					for j in range(0, n):
						A_temp[num_max][j]=-1
			#теперь здесь переделать
			else:  #в столбце с max числом нулей все элементы делаем =-1
				if(null_count[num_max]==1):
					#находим номер строки, в которой содержится этот ноль
					str_num=-1
					for i in range(0, n):
						if(A_temp[i][num_max]==0.0):
							str_num=i
							break
					#находим число -1 в столбце
					col_count=0
					for i in range(0, n):
						if(A_temp[i][num_max]==-1):
							col_count=col_count+1
					#находим число -1 в строке
					str_count=0
					for j in range(0, n):
						if(A_temp[str_num][j]==-1):
							str_count=str_count+1
					if(str_count > col_count):   #вычеркиваем строку
						for j in range(0, n):
							A_temp[str_num][j]=-1
						num_zero_string.append(str_num)
					else:   #вычеркиваем столбец
						for i in range(0, n):
							A_temp[i][num_max]=-1
						num_zero_column.append(num_max)
				else:
					num_zero_column.append(num_max-n)
					for i in range(0, n):
						A_temp[i][num_max-n]=-1

			#Проверка матрицы A_temp на наличие нулей
			zero_in_A=False
			for i in range(0, n):
				for j in range(0, n):
					if (A_temp[i][j]==0):
						zero_in_A=True
						break
				if (zero_in_A==True):
					break
		#находим минимум среди всех ненулевых элементов в A_temp
		no_zero_arr=[]
		for i in range(0, n):
			for j in range(0, n):
				if (A_temp[i][j]!=-1):
					no_zero_arr.append(A_temp[i][j])
		min_temp=min(no_zero_arr)
		for i in range(0, n): #вычитаем min_temp из невычеркнутых элементов
			for j in range(0, n):
				if (A_temp[i][j]!=-1):
					A_temp[i][j]=A_temp[i][j]-min_temp

		no_zero_arr.clear()
		#переход к исходной матрице
		for i in range(0, n): #
			for j in range(0, n):
				if (A_temp[i][j]!=-1):
					A[i][j]=A_temp[i][j]

		# к элементам в пересечениях зачеркнутых линий прибавляем min
		for i in range(0, len(num_zero_string)):
			for j in range(0, len(num_zero_column)):
				A[num_zero_string[i]][num_zero_column[j]]=A[num_zero_string[i]][num_zero_column[j]]+min_temp
	
		#Начало пункта 3, выделяем нули
		A_temp2=copy.deepcopy(A)
		while(1):
			null_count=[] #сначала смотрим строки (находим число нулей)
			for i in range (0, n):
				count=0
				for j in range(0, n):
					if(A_temp2[i][j]==0):
						count=count+1
				null_count.append(count)
			for j in range (0, n): #потом смотрим столбцы в порядке возрастания  (находим число нулей)
				count=0
				for i in range(0, n):
					if(A_temp2[i][j]==0):
						count=count+1
				null_count.append(count)
	
			null_in_matrix=False
			for i in range(0, 2*n):
				if(null_count[i]!=0):
					null_in_matrix=True
			if(null_in_matrix==False):
				break
	
			min1=min_null(null_count) #(min)
			num_min1=0
			num_min2=0
			for i in range(0, 2*n):
				if(null_count[i]==min1):
					num_min1=i
					break
			num_null=[]
			if(num_min1<n): #(выбрано 0 в строке), НЕ ПРОВЕРЕНО  (num_min1-в строке, num_min2 - в столбце)
				null_count2=[]
				for j in range(0, n):
					if(A_temp2[num_min1][j]==0):
						num_null.append(j)
				for i in range(0, len(num_null)): #записываем число нулей в строках
					null_count2.append(null_count[num_null[i]])
				min2=min_null(null_count2)#находим минимальное число нулей среди столбцов (min)
				for i in range(0, len(null_count2)):#находим номер элемента массива, содержащий номер столбца с минимальным числом нулей
					if(null_count2[i]==min2):
						num_min2=i
						break
				num_min2=num_null[num_min2]#находим номер строки
				num_min1=num_min1
				for i in range (0, n):
					A_temp2[num_min1][i]=-1
				for i in range (0, n):
					A_temp2[i][num_min2]=-1
				null_arr.append(mesh(num_min1, num_min2))

			else: #ищем num_min2 (выбрано 0 в столбце)  (num_min1-в столбцe, num_min2 - в строке)
				null_count2=[]
				for i in range(0, n): #находим номера строк, в которых есть нули
					if(A_temp2[i][num_min1-n]==0):
						num_null.append(i)
				for i in range(0, len(num_null)): #записываем число нулей в строках
					null_count2.append(null_count[num_null[i]])
				min2=min_null(null_count2)#находим минимальное число нулей среди строк  (min)
				for i in range(0, len(null_count2)):#находим номер элемента массива, содержащий номер строки с минимальным числом нулей
					if(null_count2[i]==min2):
						num_min2=i
						break
				num_min2=num_null[num_min2]#находим номер строки
				num_min1=num_min1-n
				for i in range (0, n):
					A_temp2[num_min2][i]=-1
				for i in range (0, n):
					A_temp2[i][num_min1]=-1
				null_arr.append(mesh(num_min2, num_min1))
			null_count.clear()
		A_temp2.clear()
		A_temp.clear()
		num_zero_string.clear()
		num_zero_column.clear()
		#КОНЕЦ ЦИКЛА

	res=0
	n=len(null_arr)
	for i in range(0, n):
		res=res+M[null_arr[i].string][null_arr[i].column]
	return(res)







print("res = ", vengersky_algoritm(A1))


