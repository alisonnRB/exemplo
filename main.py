from drawlib.apis import * #type: ignore
# função que imprime "Hello World!"
#print("Hello World!")

# for i in range (171):
#     print("Hello World!")

config(width=100, height=100)


line((10, 10), (90, 90))

circle((25, 75), radius=20)

text((75, 5), "Hello drawlib!")


save()