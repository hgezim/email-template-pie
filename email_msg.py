#!/usr/bin/env python

import re
import os
import richxerox

if __name__ == "__main__":

	file_names = filter(lambda file: "." in file and file.rsplit(".",1)[1] == "msg" ,os.listdir("."))
	if len(file_names) > 1:
		print "Choose your message:"

		for i, file_name in enumerate(file_names):
			print "{0}. {1}".format(i, file_name.rsplit(".", 1)[0])

		choice = int(raw_input(":"))

	chosen_file_name = file_names[choice]
	file = open(chosen_file_name)
	lines = file.readlines()

	out_lines = []
	vars = {}
	for line in lines:
		re_results = re.search('{{([a-zA-Z0-9 ]+)}}', line)
		if re_results:
			var_name = re_results.group(1)
			whole_var = re_results.group(0)
			if var_name not in vars.keys():
				user_response = raw_input("{0}:".format(var_name))
				vars[var_name] = user_response
			line = line.replace(whole_var, vars[var_name])
		out_lines.append(line)

	message = "".join(out_lines)

        richxerox.copy(text=message)
	print message
        print ""
	print "Copied to clipboard."
