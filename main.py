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
	for item in row['items']:
		timestamp.append(row['ordered_time'])
		if item in items_a:
			tmp_ind = items_a.index(item)
			tmp_item = items_arr[tmp_ind].split('_')
			tmp_item[1] = int(tmp_item[1])+1
			items_arr = tmp_item[0]+"_"+str(tmp_item[1])
		else:
			items_a.append(item)
			items_arr.append(item+"_1"+)
			cust_id.append(row['customer_id'])
for rating in items_arr:
	num = rating.split("_")
	final_rat = 3+((num-1)*2/n^2)
	ratings.append(final_rat)

new_data = {'userId': cust_id, 'movieId': items_a, 'rating': ratings, 'timestamp': timestamp}
updated_df = pd.DataFrame(data = new_data)
updated_df.to_csv('ratings.csv')

	try:
		new_dict[row["customer_id"]].append(str(row["restaurant_id"])+"_"+str(row["order_id"]))
	except KeyError:
		new_dict[row["customer_id"]] = [str(row["restaurant_id"])+"_"+str(row["order_id"])]
	row_num = row_num+1

id_keys = []
receiver_val = []
for key in new_dict.keys():
	id_keys.append(key)
	receiver_val.append(str(new_dict[key])[1:-1])

new_data = {'receiver': id_keys, 'receiver_value': receiver_val}
updated_df = pd.DataFrame(data = new_data)
updated_df.to_csv('message_1_1.csv')


time = None
tf = 0
new_dict = {}
new_dict_t = {}
row_num = 0
for index, row in c.iterrows():
	if row_num%1000 == 0:
		print row_num
	tmp = row['ordered_time'].split(' ')
	new_time = [tmp[0],tmp[1].split(':')[0]]
	tmp_time = "_".join(new_time)
	tmp_time_t = str(tmp_time)+'_c'
	# loc_u = Geohash.decode_exactly(row['customer_geohash'])[:2]
	if time==None:
		time = new_time
		# new_dict[tmp_time] = [loc_u]
		new_dict_t[tmp_time_t] = [row['items']]
	elif new_time[0]==time[0] and int(new_time[1])-int(time[1])==0:
		# try:
		# new_dict[tmp_time].append(loc_u)
		new_dict_t[tmp_time_t].append(row['items'])
		# except KeyError:
		# new_dict[tmp_time] = [(loc_u)]
	else:
		# new_dict[tmp_time] = [(loc_u)]
		new_dict_t[tmp_time_t] = [row['items']]
	time = new_time
	row_num = row_num+1

time_keys = []
# geo_codes = []
items = []
for key in new_dict_t.keys():
	time_keys.append(key)
	# geo_codes.append(str(new_dict[key])[1:-1])
	key = str(key)
	items.append(new_dict_t[key])

new_data = {'time': time_keys, 'items': items}
updated_df = pd.DataFrame(data = new_data)

import ast
# for index, row in updated_df.iterrows():
items_w = []
row = updated_df.loc[0]
tmp_items = row['items']
tmp_items = ast.literal_eval(tmp_items)
for item in tmp_items:
		item = item[1:-1].split(', ')
		for i in item:
			try:
				print i
				w = df_2[df_2['item_id']==int(i)]['dish_family']
				q = np.array(w)
				q = q[0]
				items_w.append(q)
			except Exception as e:
				print e

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

wordcloud = WordCloud(stopwords=STOPWORDS,
                          background_color='white', 
                      max_words=300
                         ).generate(word_str)
plt.clf()
plt.imshow(wordcloud)
plt.axis('off')
(-0.5, 399.5, 199.5, -0.5)
plt.show()