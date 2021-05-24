from database import engine, tagcounter_db, select_from_db
import functions as fc
import logging
import argparse
import pickle
from tld import get_tld
from datetime import datetime
import tkinter as tk


# add logging
logging.basicConfig(level=logging.INFO,
                    filename='tagcounter_log.log',
                    filemode='a',
                    format='%(asctime)s  - %(message)s')


# Create the parser
def parse_tagcounter_args():
    if __name__ == "__main__":
        my_parser = argparse.ArgumentParser(prog='tagcounter',
                                            description='Count tags of an html-file')
        # Add the arguments
        my_parser.add_argument('--get',
                               type=str,
                               help='get tags and their counts')
        my_parser.add_argument('--view',
                               help='fetch data from the database')

    # Execute the parse_args() method
    args = my_parser.parse_args()
    # print(type(args))

    return args


args = parse_tagcounter_args()

parsed_yaml_file = fc.parse_yaml_file()  # parse yaml-file

if args.get is not None:  # tagcounter --get url
    # check if synonym exists in synonyms.yaml, then use it to build an object
    if args.get in parsed_yaml_file.keys():
        Sample = fc.ContaTags(parsed_yaml_file[args.get])
    else:
        Sample = fc.ContaTags(args.get)

    cmd_tagcount_dict = Sample.run()  # returns a dictionary object
    # Pickle the Python object: convert the object into a byte stream
    pickled_cmd_tagcount_dict = pickle.dumps(cmd_tagcount_dict,
                                             protocol=None,
                                             fix_imports=True)
    # extract 2nd level domain name: 'google' (передаем туда весь урл (ошибка))
    site = get_tld(fc.url, as_object=True)
    domain = site.domain
    # check data in tags.db: update if exists, insert if not
    connection = engine.connect()
    check = tagcounter_db.select().where(tagcounter_db.c.url == fc.url)
    check_result = connection.execute(check).scalar()  # returns True / False
    if check_result:
        update_data = tagcounter_db.update().where(tagcounter_db.c.url
                                                   == fc.url).values(
                                                   site_name=domain,
                                                   url=fc.url,
                                                   date_time=datetime.now(),
                                                   tagcount=pickled_cmd_tagcount_dict)
        connection.execute(update_data)
        print("Data successfully updated!")
    else:
        insert_data = tagcounter_db.insert().values(
                      site_name=domain,
                      url=fc.url,
                      date_time=datetime.now(),
                      tagcount=pickled_cmd_tagcount_dict)
        connection.execute(insert_data)
        print("Data successfully loaded into Database!")

    connection.close()
    # print(cmd_tagcount_dict)

elif args.view is not None:  # tagcounter --view url
    # check if synonym exists in synonyms.yaml, then use it
    user_input = args.view
    if user_input in parsed_yaml_file.keys():
        user_input = parsed_yaml_file[user_input]
    else:
        user_input

    # check if we enter an URL without the protocol, if we don't, add protocol
    full_url = fc.add_protocol_to_url(user_input)
    results = select_from_db(full_url)  # connect to DB and execute select
    # print(results)
    results = results[0][0]  # extract pickled object from the results list
    fc.unpickle_db_results(results)  # unpickle results from DB


elif args.view is None and args.get is None:  # tagcounter
    def load_from_db():
        gui_user_input = txt.get()
        # print(user_input)
        if gui_user_input in parsed_yaml_file.keys():
            gui_user_input = parsed_yaml_file[gui_user_input]
        else:
            gui_user_input

        # add protocol to url
        gui_full_url = fc.add_protocol_to_url(gui_user_input)
        gui_results = select_from_db(gui_full_url)  # select from DB
        # print(results)
        gui_results = gui_results[0][0]  # extract pickled object
        gui_unpickled_result = fc.unpickle_db_results(gui_results) # unpickle results 
        output.delete(1.0, tk.END)  # clean the output box before insert
        result_load_from_db = "{}: ".format(txt.get()) + str(gui_unpickled_result)
        output.insert(tk.END, result_load_from_db)
        statusbar.configure(text="I've counted tags for you!")

    def load_from_internet():
        gui_user_input_inet = txt.get()
        if gui_user_input_inet in parsed_yaml_file.keys():
            SampleObject = fc.ContaTags(parsed_yaml_file[gui_user_input_inet])
        else:
            SampleObject = fc.ContaTags(gui_user_input_inet)

        # print(gui_user_input_inet)
        gui_tagcount_dict = SampleObject.run()
        result_load_from_internet = "{}: ".format(txt.get()) + str(gui_tagcount_dict)
        output.delete(1.0, tk.END)  # clean the output box before insert
        output.insert(tk.END, result_load_from_internet)
        statusbar.configure(text="I've counted tags for you!")

    window = tk.Tk()
    window.title("Welcome to Tagcounter!")
    window.geometry('600x450')
    text = tk.Label(window, text="Enter url, please")
    text.grid(column=1,
              row=0,
              columnspan=2,
              sticky=tk.E,
              pady=10,
              padx=10)
    txt = tk.Entry(window, width=30)
    txt.focus()
    txt.grid(column=3,
             row=0,
             columnspan=2,
             sticky=tk.W+tk.E,
             pady=10,
             padx=10)
    btn_internet = tk.Button(window,
                             text="Download From Internet",
                             command=load_from_internet)
    btn_internet.grid(column=4, row=3, padx=10, pady=10, sticky=tk.E)
    btn_db = tk.Button(window, text="Show From DB", command=load_from_db)
    btn_db.grid(column=3, row=3, sticky=tk.W, pady=10, padx=10)
    output = tk.Text(window, height=10, width=45)
    output.grid(column=2, row=4, columnspan=3, pady=10, padx=10)
    scroll = tk.Scrollbar(command=output.yview)
    scroll.grid(column=5, row=4)
    output.config(yscrollcommand=scroll.set)
    statusbar = tk.Label(window,
                         text="waiting for the url…",
                         bd=1, relief=tk.SUNKEN,
                         anchor=tk.W)
    statusbar.grid(column=0,
                    row=6,
                    columnspan=5,
                    sticky=tk.W+tk.E,
                    pady=10,
                    padx=10)
    window.mainloop()
