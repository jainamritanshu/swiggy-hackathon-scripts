import pandas as pd
df = pd.read_csv("/run/user/7406149/gvfs/smb-share:server=172.16.120.10,share=hackathon/Dataset_1_Order_Data/order_data.csv")

new_dict = {}
row_num = 0
cust_id = []
items_arr = []
items_a = []
ratings = []
timestamp = []
df = df.sort_values(['customer_id'])
for index, row in df.iterrows():
	if row_num%1000 == 0:
		print row_num
	if row_num==100000:
		break
	import ast
	try:
		tmp_items = row['items']
		tmp_items = ast.literal_eval(tmp_items)
		for item in tmp_items:
			print item
			if item in items_a:
				tmp_ind = items_a.index(item)
				tmp_item = items_arr[tmp_ind].split('_')
				print tmp_item
				tmp_item[1] = int(tmp_item[1])+1
				items_arr[tmp_ind] = tmp_item[0]+"_"+str(tmp_item[1])
			else:
				items_a.append(str(item))
				items_arr.append(str(item)+"_1")
				cust_id.append(row['customer_id'])
				timestamp.append(row['ordered_time'])
		row_num+=1
	except Exception as e:
		print e
for rating in items_arr:
	num = int(rating.split("_")[1])
	tmp = float(num-1)*float(2)/float(num**2)
	final_rat = 3+tmp
	ratings.append(final_rat)

new_data = {'userId': cust_id, 'movieId': items_a, 'rating': ratings, 'timestamp': timestamp}
updated_df = pd.DataFrame(data = new_data)
updated_df.to_csv('ratings.csv')