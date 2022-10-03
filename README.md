# ebay_rest
A Python 3 pip package that wraps eBay’s REST APIs.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ebay_rest.

```bash
pip install ebay_rest    # Use pip3 if your computer also has Python 2 installed.
```

If you are one of the few people who want ebay_rest to get user tokens, do the following.

Install [Chrome](https://www.google.ca/chrome/).

```bash
pip install selenium    # Use pip3 if your computer also has Python 2 installed.
```

Install [Webdriver](https://sites.google.com/chromium.org/driver/), aka Chromedriver, for your version of Chrome .

Here is a method for installing Webdriver/Chromedriver on macOS and tweaking security to permit it.

Install [HomeBrew](https://brew.sh)
```bash
brew install chromedriver
```
```bash
cd /usr/local/Caskroom/chromedriver
```
cd to the subdirectory that matches your Chrome version, e.g., 91.0.4472.101
```bash
xattr -d com.apple.quarantine chromedriver
```
## Setup

Follow the instructions [here](https://github.com/matecsaj/ebay_rest/blob/main/tests/ebay_rest_EXAMPLE.json). 

## Usage

```python
from ebay_rest import API, DateTime, Error, Reference

print(f"eBay's official date and time is {DateTime.to_string(DateTime.now())}.\n")

print("All valid eBay global id values, also known as site ids.")
print(Reference.get_global_id_values(), '\n')

try:
    api = API(application='production_1', user='production_1', header='US')
except Error as error:
    print(f'Error {error.number} is {error.reason}  {error.detail}.\n')
else:
    try:
        print("The five least expensive iPhone things now for sale on-eBay:")        
        for record in api.buy_browse_search(q='iPhone', sort='price', limit=5):
            if 'record' not in record:
                pass    # TODO Refer to non-records, they contain optimization information.
            else:
                item = record['record']
                print(f"item id: {item['item_id']} {item['item_web_url']}")
    except Error as error:
        print(f'Error {error.number} is {error.reason} {error.detail}.\n')
    else:
        pass

print("\nClass documentation:")
print(help(API))    # Over a hundred methods are available!
print(help(DateTime))
print(help(Error))
print(help(Reference))
```

## FAQ - Frequently Asked Questions

**Question:** How are API results organized?

**Answer:**  
* Elemental information is stored in dates, integers, strings and other basic [built-in types](https://docs.python.org/3/library/stdtypes.html).
* [Dictionaries](https://docs.python.org/3/library/stdtypes.html#dict) contain related elements.
* [Lists](https://docs.python.org/3/library/stdtypes.html#list) contain information organized repetitively; expect zero or more contents.
* Dicts and Lists may be nested.
* eBay classifies data as optional or mandatory. Optional elements, dicts or lists are omitted. Manditories have a [None](https://docs.python.org/3/library/constants.html?highlight=none#None) value.

##
**Q:** How are paged calls/results handled? 

**A:** A [simple generator](https://www.python.org/dev/peps/pep-0255/#specification-yield) is implemented.
* To be clear, "Paging" is eBay's term for repeating a call while advancing a record offset to get all records.
* eBay documentation has the word "Page" in the return type of paging calls. 
* Do NOT supply a record "offset" parameter when making a paging call.
* The "limit" parameter is repurposed to control how many records from the entire set you want.
* To get all possible records, don't supply a limit.
* eBay imposes a hard limit on some calls, typically 10,000 records. Use filters to help keep below the limit. Use try-except to handle going over.
* Avoid exhausting memory by making the call within a ["for" loop](https://docs.python.org/3/reference/compound_stmts.html#for).

##
**Q:** What should I do when the browser pop-up happens? 

**A:** Watch and be ready to act.
* At the beginning, you may see a captcha; you need to complete it within 30-seconds.
* Near the end, you may see a 2FA (two-factor authentication) prompt; you need to complete it within 30-seconds.
* Otherwise, be patient, give the whole thing up to 2-minutes to complete, the pop-up will close automatically.

##
**Q:** Can the browser pop-up be stopped? 

**A:** Reusing the result of the browser pop-up is possible. After running your program, check your terminal/console or [info level logger](https://docs.python.org/3.7/library/logging.html).

##
**Q:** Why is eBay giving an "Internal Error" or "Internal Server Error"? 

**A:** Rapidly repeating an API call with the same parameter values can trigger this.
##
**Q:** Parallelism, is it safe to do [treading](https://docs.python.org/3/library/threading.html) or [multiprocessing](https://docs.python.org/3/library/multiprocessing.html)?

**A:** Yes, for treading. Multiprocessing is unknown, [help wanted](https://github.com/matecsaj/ebay_rest/issues/20).
##
**Q:** How to optimize API calls?

**A:** Prioritized, do the first things first.
1. Cache results to avoid repeating calls with identical parameter values.
2. Some calls have filtering options; omit unneeded data.
3. When the call returns a list, make the call in a ["for" loop](https://docs.python.org/3/reference/compound_stmts.html#for). 
4. Use [threading](https://docs.python.org/3/library/threading.html) to make calls in parallel but don't exhaust RAM.
5. Use multiprocessing. -- Multiprocessing support is a [goal](https://github.com/matecsaj/ebay_rest/issues/20). -- A safe workaround is to concurrently run copies of your program and divide the work among each.
6. Reuse the API object.
7. Switch to a faster internet connection. 
8. Switch to computer with faster cores.

##
**Q:** How to get data from a response header?

**A:** As is this library can't get the data, pick a workaround.
1. In some cases, another call can get the information; a demonstration is in the [unit tests](https://github.com/matecsaj/ebay_rest/blob/main/tests/ebay_rest.py), search for test_sell_feed_create_inventory_task and task_id_new.
2. You could fork this library, and hack the call you need, so that it returns that needed data.
3. You could write your only code from scratch to make the RestFul call.
* [Swagger](https://swagger.io/tools/swagger-codegen/) with OpenAPI contracts from eBay generate the core of this library, and they are not currently able to return response header data. Please ask eBay to solve the root problem; many voices will convince them of the need to act.

## Contributing
* Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
* Note the error number guide documented in the Error class definition. 
* Please make sure to update unit tests as appropriate.
* Release Steps 
  1. in the root directory of the project, run CLI commands
     1. brew update
     2. brew upgrade
     3. python -m pip install --upgrade pip
     4. pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
     5. pipreqs --print src
  2. edit the setup.cfg file
     1. update the section install_requires  per the output from pipregs
     2. advance the version number
  3. repeat until error-free 
     1. run /ebay_rest/scripts/generate_code.py
     2. run /test/ebay_rest.py
     3. resolve any errors but don't directly edit the code generated by generate_code.py
  4. in the root directory of the project, run CLI commands
     1. python3 -m build
     2. python3 -m twine upload dist/*0.0.XX*
        1. in place of 0.0.xx put the new version number
        2. username: \_\_token\_\_
        3. password: your token

## Legal
* [MIT](https://github.com/matecsaj/ebay_rest/blob/main/LICENSE) licence.
* "Python" is a trademark of the [Python Software Foundation](https://www.python.org/psf/).
* "eBay" is a trademark of [eBay Inc](https://www.ebay.com).
* Official endorsement by [eBay Inc](https://www.ebay.com) is not claimed or implied.
* The origin of the oath code is [eBay Oauth Python Client](https://github.com/eBay/ebay-oauth-python-client).