import base64
# #todo png or jpg ???????
# with open('img.png', 'rb') as img:
#     encode_img = base64.encodebytes(img.read())
#     print(encode_img)









# with open('img.png', 'rb') as img:
#     encode_img = base64.encodebytes(img.read())
#     print(img.seek(0), img.read())
#     print(encode_img)

#
# b'iVBORw0KGgoAAAANSUhEUgAAATYAAAE2AQAAAADDx4MEAAACRUlEQVR4nO2aS4rcMBRFz4sEPZQh\nC+ilqHbQS2qypOzAWkotoMAeNljcDCTVJ6OGgMpxSQPjKh+wHo/3u7KJ76z841sYDO7fODTf3Tlp\nDhKEDaK29ihse7fjKByagyRpQ1qAWC5ORG1IkjQPf/TksplNQHpvAZGmbKQJSGb27P29KhfPbwKc\niJJKpPR47+Buy9/dp5NDrKA0Xfxjod+7HUfinFrpyGancEtaUCLlyft7Jc7DavU+fWz+r9Coj8Lu\n7TgKVzuo1kZdGyo9rtFfdeKaPxaQlvv5o7inXfZux1E4qgNwgiBVp+CkuTzdGPHRj7tO5VuZ1CWp\nembGFUcNf3TlSkPlZJ+S7ES2oqHEpcbHk/f3UlypGnX2q7mp/lfWqB9duZql5pqWuC8dOBGXka96\nch7CxVtUNuLvnwKyCcCisokVSB+XvdtxFK51UIurXa4Wp5rDmog14qMf52F9u0WFjPBlInwZkL2K\nyDvioxdXO6jY4oOi7y5tMGmFfu92HIXzsHqAbJShsETKdhV+3Ub62L0dB+LafK6ZbHYCzOytTCJA\nNuLyP9hxIE6/pmwtUkBz+Ko/0/vQ23tyj/qu1EbzJmeV+XzUj17c/fclt6Z3bq6o7hn9bi/OQ1gA\nsiedMLF6LJ4N1fLuNnvi/l6N45qRyvc+VwGxrXocsnc7DskFyT7P/k5jrBr86K+ewq1mJSDSe1UW\nYfXYaSf7ewHO06ZAIAhYJxTPBlU5uZjSNPSSTtxDf/XQ9NaTwnE+2JWz8X37rrg/VVnC1e1cBMYA\nAAAASUVORK5CYII=\n'
# decode = base64.decodebytes(b'iVBORw0KGgoAAAANSUhEUgAAATYAAAE2AQAAAADDx4MEAAACRUlEQVR4nO2aS4rcMBRFz4sEPZQh\nC+ilqHbQS2qypOzAWkotoMAeNljcDCTVJ6OGgMpxSQPjKh+wHo/3u7KJ76z841sYDO7fODTf3Tlp\nDhKEDaK29ihse7fjKByagyRpQ1qAWC5ORG1IkjQPf/TksplNQHpvAZGmbKQJSGb27P29KhfPbwKc\niJJKpPR47+Buy9/dp5NDrKA0Xfxjod+7HUfinFrpyGancEtaUCLlyft7Jc7DavU+fWz+r9Coj8Lu\n7TgKVzuo1kZdGyo9rtFfdeKaPxaQlvv5o7inXfZux1E4qgNwgiBVp+CkuTzdGPHRj7tO5VuZ1CWp\nembGFUcNf3TlSkPlZJ+S7ES2oqHEpcbHk/f3UlypGnX2q7mp/lfWqB9duZql5pqWuC8dOBGXka96\nch7CxVtUNuLvnwKyCcCisokVSB+XvdtxFK51UIurXa4Wp5rDmog14qMf52F9u0WFjPBlInwZkL2K\nyDvioxdXO6jY4oOi7y5tMGmFfu92HIXzsHqAbJShsETKdhV+3Ub62L0dB+LafK6ZbHYCzOytTCJA\nNuLyP9hxIE6/pmwtUkBz+Ko/0/vQ23tyj/qu1EbzJmeV+XzUj17c/fclt6Z3bq6o7hn9bi/OQ1gA\nsiedMLF6LJ4N1fLuNnvi/l6N45qRyvc+VwGxrXocsnc7DskFyT7P/k5jrBr86K+ewq1mJSDSe1UW\nYfXYaSf7ewHO06ZAIAhYJxTPBlU5uZjSNPSSTtxDf/XQ9NaTwnE+2JWz8X37rrg/VVnC1e1cBMYA\nAAAASUVORK5CYII=\n')
# img = open('res.png', 'wb')
# img.write(decode)




# Если 1 фото -> png
# Несколько   -> gif