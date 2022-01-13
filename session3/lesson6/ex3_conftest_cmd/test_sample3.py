# https://docs.pytest.org/en/latest/example/simple.html?highlight=addoption

def test_answer(cmdopt):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")
    assert 0  # to see what was printed



# Now we’ll get feedback on a bad argument:
# $ pytest -q --cmdopt=QQQ test_sample3.py
# ERROR: cmdopt must specify a numeric type as typeNNN


# -------------------------------------------------------------------------------------------- #
# Let’s run this without supplying our new option:
# $ pytest -q test_sample3.py

# And now run this with supplying a command line option:
# $ pytest -q --cmdopt=type2 test_sample3.py
# You can see that the command line option arrived in our test.
