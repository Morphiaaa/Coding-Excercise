

import re

class Paragraph:

    @staticmethod
    def change_date_format(paragraph):
    	output = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\2/\1/\3', paragraph)
    	return output

print(Paragraph.change_date_format('Last time it rained was on 07/25/2013 and today is 08/09/2013.'))