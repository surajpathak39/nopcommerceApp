pytest  -v -s -m "sanity" --html=Reports\report3.html testCases/ --browser chrome --capture=tee-sys 
rem pytest  -v -s -m "regression" --html=Reports\report3.html testCases/ --browser chrome --capture=tee-sys
rem pytest  -v -s -m "regression or sanity" --html=Reports\report3.html testCases/ --browser chrome --capture=tee-sys
rem pytest  -v -s -m "regression and sanity" --html=Reports\report3.html testCases/ --browser chrome --capture=tee-sys 


rem pytest  -v -s -m "sanity" --html=Reports\report4.html testCases/ --browser firefox --capture=tee-sys 
rem pytest  -v -s -m "regression" --html=Reports\report4.html testCases/ --browser firefox --capture=tee-sys
rem pytest  -v -s -m "regression or sanity" --html=Reports\report4.html testCases/ --browser firefox --capture=tee-sys
rem pytest  -v -s -m "regression and sanity" --html=Reports\report4.html testCases/ --browser firefox --capture=tee-sys 

rem pytest  -v -s -m "sanity" --html=Reports\report4.html testCases/ --browser edge --capture=tee-sys 
rem pytest  -v -s -m "regression" --html=Reports\report4.html testCases/ --browser edge --capture=tee-sys
rem pytest  -v -s -m "regression or sanity" --html=Reports\report4.html testCases/ --browser edge --capture=tee-sys
rem pytest  -v -s -m "regression and sanity" --html=Reports\report4.html testCases/ --browser edge --capture=tee-sys 




