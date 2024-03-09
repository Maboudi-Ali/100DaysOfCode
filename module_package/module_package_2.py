from shapes import rectangle, circle

r = int(input('circle radius:'))
print(f'circle area: {circle.area(r)}')
print(f'circle perimeter: {circle.perimeter(r)}')

l, w = map(int, input('length and width of rectangle: ').split())
print(f'rectangle area: {rectangle.area(l, w)}')
print(f'rectangle perimeter: {rectangle.perimeter(l, w)}')

