# https://docs.pytest.org/en/latest/example/simple.html?highlight=addoption

def test_answer(cmdopt):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")
    assert 0  # to see what was printed



# Now we’ll get feedback on a bad argument:
# $ pytest -q --cmdopt=type3 test_sample2.py
# ERROR: usage: pytest [options] [file_or_dir] [file_or_dir] [...]
# pytest: error: argument --cmdopt: invalid choice: 'type3' (choose from 'type1', 'type2')


# -------------------------------------------------------------------------------------------- #
# Let’s run this without supplying our new option:
# $ pytest -q test_sample2.py

# And now run this with supplying a command line option:
# $ pytest -q --cmdopt=type2 test_sample2.py
# You can see that the command line option arrived in our test.
