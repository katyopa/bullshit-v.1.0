from database import select_from_db, save_results
import functions as fc
import logging
import tkinter as tk


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,                    # add logging
                        filename='tagcounter_log.log',
                        filemode='a',
                        format='%(asctime)s  - %(message)s')
    args = fc.parse_tagcounter_args()

    parsed_yaml_file = fc.parse_yaml_file()                    # parse yaml-file

    if args.get is not None:                                   # tagcounter --get url
        url_get = fc.get_synonym(args.get)
        Sample = fc.CountTags(url_get)
        tagcount_dict = Sample.count_tags()                    # returns a dictionary object
        pickled_tag_dict = fc.pickle_tag_dict(tagcount_dict)   # pickle dict to write to db
        full_url_get = fc.add_protocol_to_url(url_get)
        domain = fc.get_domain_site_by_url(full_url_get)       # extract 2nd level domain name
        save_results(full_url_get, domain, pickled_tag_dict)   # save results to db
        print(tagcount_dict)

    elif args.view is not None:                                # tagcounter --view url
        url_view = fc.get_synonym(args.view)
        full_url = fc.add_protocol_to_url(url_view)
        results = select_from_db(full_url)                     # connect to DB and execute select
        results = results[0][0]                                # extract pickled object from the results list
        print(fc.unpickle_db_results(results))                 # unpickle results from DB

    elif args.view is None and args.get is None:               # tagcounter
        NewGuiWindow = fc.GuiWindow()
        NewGuiWindow.start()
        # window = tk.Tk()
        # window.title("Welcome to Tagcounter!")
        # window.geometry('600x450') 
        # text = tk.Label(window, text="Enter url, please")
        # text.grid(column=1,
        #         row=0,
        #         columnspan=2,
        #         sticky=tk.E,
        #         pady=10,
        #         padx=10)
        # txt = tk.Entry(window, width=30)
        # txt.focus()
        # txt.grid(column=3,
        #         row=0,
        #         columnspan=2,
        #         sticky=tk.W+tk.E,
        #         pady=10,
        #         padx=10)
        # btn_internet = tk.Button(window,
        #                         text="Download From Internet",
        #                         command=load_from_internet)
        # btn_internet.grid(column=4, row=3, padx=10, pady=10, sticky=tk.E)
        # btn_db = tk.Button(window, text="Show From DB", command=load_from_db)
        # btn_db.grid(column=3, row=3, sticky=tk.W, pady=10, padx=10)
        # output = tk.Text(window, height=10, width=45)
        # output.grid(column=2, row=4, columnspan=3, pady=10, padx=10)
        # scroll = tk.Scrollbar(command=output.yview)
        # scroll.grid(column=5, row=4)
        # output.config(yscrollcommand=scroll.set)
        # statusbar = tk.Label(window,
        #                     text="waiting for the url…",
        #                     bd=1, relief=tk.SUNKEN,
        #                     anchor=tk.W)
        # statusbar.grid(column=0,
        #                 row=6,
        #                 columnspan=5,
        #                 sticky=tk.W+tk.E,
        #                 pady=10,
        #                 padx=10)
        # window.mainloop()

