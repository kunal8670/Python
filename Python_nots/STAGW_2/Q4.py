#You want to hide the actual password is static (not the whole line), so it becomes:
#-->log = "User admin logged in with password=****"

log = "User admin logged in with password=1234"
print(log.replace('1234','****'))

#You want to hide the actual passwordid dynamic(not the whole line), so it becomes:
#-->log = "User admin logged in with password=****"


log = "User admin logged in with password=1234"
head, sep, tail = log.partition("=")
masked_log = head + sep + "****"
print(masked_log)
