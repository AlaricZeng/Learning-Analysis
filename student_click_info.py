import csv
from datetime import datetime
from FileOperation import FileOperation

# with open('C:/Users/alari/Desktop/assignmentclickrecords_261.csv', 'rt') as f:
# 	reader = csv.reader(f, delimiter = ',', skipinitialspace=True)
# 	fileOperation.GetContent() = list()
# 	cols = next(reader)

# 	for line in reader:
# 		if line[0] != "":
# 			fileOperation.GetContent().append(line)
READ_PATH = 'C:/Users/alari/Desktop/assignmentclickrecords_261.csv'
WRITE_PATH = 'C:/Users/alari/Desktop/student_click_info.csv'
SUBMISSION_PATH = 'C:/Users/alari/Desktop/new.csv'


fileOperation = FileOperation(READ_PATH, WRITE_PATH)
fileOperation.ReadFile(',', True)

submission_Info = FileOperation(SUBMISSION_PATH, '')
submission_Info.ReadFile(',', True)

def __datetime(date_str):
	return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

#Student_Click_Info: [user_id, Assignment, click_time, first_click, last_click, Duration]
Student_Click_Info = [[0 for i in range(7)]]
USER_ID = 0
ASSIGNMENT = 1
CLICK_TIME = 2
FIRST_CLICK = 3
LAST_CLICK = 4
DURATION = 5

SubOfStudent = 0

#Clean data
data_List = list()
for i in range(len(fileOperation.GetContent())):
	if fileOperation.GetContent()[i][3] == 'Access Assignment 1':
		if fileOperation.GetContent()[i][2] >= '2016-09-21 23:59:00':
			for j in range(len(submission_Info.GetContent())):
				if fileOperation.GetContent()[i][1] == submission_Info.GetContent()[j][0] and\
					submission_Info.GetContent()[j][2] == '250000005483340':
					if submission_Info.GetContent()[j][1] != 'NULL':
						if fileOperation.GetContent()[i][2] <= submission_Info.GetContent()[j][1]:
							data_List.append(fileOperation.GetContent()[i])
					else:
						if fileOperation.GetContent()[i][2] <= '2016-09-28 23:59:00':
							data_List.append(fileOperation.GetContent()[i])
	elif fileOperation.GetContent()[i][3] == 'Access Assignment 2':
		if fileOperation.GetContent()[i][2] >= '2016-09-29 00:00:00':
			for j in range(len(submission_Info.GetContent())):
				if fileOperation.GetContent()[i][1] == submission_Info.GetContent()[j][0] and\
					submission_Info.GetContent()[j][2] == '250000005507263':
					if submission_Info.GetContent()[j][1] != 'NULL':
						if fileOperation.GetContent()[i][2] <= submission_Info.GetContent()[j][1]:
							data_List.append(fileOperation.GetContent()[i])
					else:
						if fileOperation.GetContent()[i][2] <= '2016-10-05 23:59:59':
							data_List.append(fileOperation.GetContent()[i])
	elif fileOperation.GetContent()[i][3] == 'Assignment: Database Design':
		if fileOperation.GetContent()[i][2] >= '2016-09-11 23:59:00':
			for j in range(len(submission_Info.GetContent())):
				if fileOperation.GetContent()[i][1] == submission_Info.GetContent()[j][0] and\
					submission_Info.GetContent()[j][2] == '250000005483339':
					if submission_Info.GetContent()[j][1] != 'NULL':
						if fileOperation.GetContent()[i][2] <= submission_Info.GetContent()[j][1]:
							data_List.append(fileOperation.GetContent()[i])
					else:
						if fileOperation.GetContent()[i][2] <= '2016-09-19 23:59:00':
							data_List.append(fileOperation.GetContent()[i])

for i in range(len(data_List)):
	if data_List[i][1] == Student_Click_Info[SubOfStudent][USER_ID]:
		temp_SubOfStudent = SubOfStudent
		if_Exit = False
		if data_List[i][3] != Student_Click_Info[SubOfStudent][ASSIGNMENT]:
			while data_List[i][1] == Student_Click_Info[temp_SubOfStudent][USER_ID]:
				if data_List[i][3] == Student_Click_Info[temp_SubOfStudent][ASSIGNMENT]:
					if_Exit = True
					break
				else:
					temp_SubOfStudent -= 1
			if if_Exit == True:
				Student_Click_Info[temp_SubOfStudent][CLICK_TIME] += 1
				if data_List[i][2] < Student_Click_Info[temp_SubOfStudent][FIRST_CLICK]:
					Student_Click_Info[temp_SubOfStudent][FIRST_CLICK] = data_List[i][2]
					Student_Click_Info[temp_SubOfStudent][DURATION] = (__datetime(Student_Click_Info[temp_SubOfStudent][LAST_CLICK]) -\
																 __datetime(Student_Click_Info[temp_SubOfStudent][FIRST_CLICK])).days
				if data_List[i][2] > Student_Click_Info[temp_SubOfStudent][LAST_CLICK]:
					Student_Click_Info[temp_SubOfStudent][LAST_CLICK] = data_List[i][2]
					Student_Click_Info[temp_SubOfStudent][DURATION] = round((__datetime(Student_Click_Info[temp_SubOfStudent][LAST_CLICK]) -\
																 __datetime(Student_Click_Info[temp_SubOfStudent][FIRST_CLICK])).total_seconds() / (3600 * 24), 5)
			else:
				Student_Click_Info.append([data_List[i][1], data_List[i][3], 1, data_List[i][2], data_List[i][2], 0])
				SubOfStudent += 1
		else:
			Student_Click_Info[temp_SubOfStudent][CLICK_TIME] += 1
			if data_List[i][2] < Student_Click_Info[temp_SubOfStudent][FIRST_CLICK]:
				Student_Click_Info[temp_SubOfStudent][FIRST_CLICK] = data_List[i][2]
				Student_Click_Info[temp_SubOfStudent][DURATION] = round((__datetime(Student_Click_Info[temp_SubOfStudent][LAST_CLICK]) -\
															 __datetime(Student_Click_Info[temp_SubOfStudent][FIRST_CLICK])).total_seconds() / (3600 * 24), 5)
			if data_List[i][2] > Student_Click_Info[temp_SubOfStudent][LAST_CLICK]:
				Student_Click_Info[temp_SubOfStudent][LAST_CLICK] = data_List[i][2]
				Student_Click_Info[temp_SubOfStudent][DURATION] = round((__datetime(Student_Click_Info[temp_SubOfStudent][LAST_CLICK]) -\
															 __datetime(Student_Click_Info[temp_SubOfStudent][FIRST_CLICK])).total_seconds() / (3600 * 24), 5)
	else:
		Student_Click_Info.append([data_List[i][1], data_List[i][3], 1, data_List[i][2], data_List[i][2],0])
		SubOfStudent += 1

USER_INFO_FILE = 'C:/Users/alari/Desktop/MISY261&262 roster.csv'
fileOperation1 = FileOperation(USER_INFO_FILE, '')
fileOperation1.ReadFile(',', True)

for i in range(len(Student_Click_Info)):
	for j in range(len(fileOperation1.GetContent())):
		if Student_Click_Info[i][0] == fileOperation1.GetContent()[j][-1]:
			Student_Click_Info[i].append(fileOperation1.GetContent()[j][1])
			break

Student_Click_Info_Not_Null = list()

for i in range(len(Student_Click_Info)):
	if len(Student_Click_Info[i]) > DURATION + 1:
		Student_Click_Info_Not_Null.append(Student_Click_Info[i])

Student_Click_Info_Not_Null[0][0] = 'User_id'
Student_Click_Info_Not_Null[0][1] = 'Assignment'
Student_Click_Info_Not_Null[0][2] = "Click_Time"
Student_Click_Info_Not_Null[0][3] = 'First_Click'
Student_Click_Info_Not_Null[0][4] = 'Last_Click'
Student_Click_Info_Not_Null[0][5] = 'Duration'
Student_Click_Info_Not_Null[0][6] = 'SYS_USER_ID'

#fileOperation.WriteFile(Student_Click_Info_Not_Null)

HOMEWORK = 'Assignment: Database Design'
with open('C:/Users/alari/Desktop/TEMP.csv', 'w') as f:
	for i in range(len(Student_Click_Info)):
		if Student_Click_Info[i][1] == HOMEWORK and len(Student_Click_Info[i]) > DURATION + 1:
			for j in range(len(Student_Click_Info[i]) - 1):
				f.write("%s," % Student_Click_Info[i][j])
			f.write("%s\n" % Student_Click_Info[i][len(Student_Click_Info[i]) - 1])


