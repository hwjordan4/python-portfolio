#!c:/python34/python.exe

__author__ = 'Ben'

from request import request_to_sakila


if __name__ == "__main__":
    path = "/customer"
    resp = request_to_sakila(path)

    doc1 = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Customer List</title>
                <link href='/style1.css' rel='stylesheet' type='text/css'/>
            </head>
            <body>
    """
    doc2 = """
            </body>
        </html>
    """

    print("Content-type: text/html")
    print()
    print(doc1)
    if resp[0] == 'K':
        print("<table class='grid'>")
        print("<thead>")
        print("""
            <tr>
            <th>ID</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Email</th>
            <th>Address</th>
            </tr>
        """)
        print("</thead>")
        print("<tbody>")
        for row in resp[1]:
            row_pic = """
                <tr>
                    <td>{0[customer_id]}</td>
                    <td>{0[first_name]}</td>
                    <td>{0[last_name]}</td>
                    <td>{0[email]}</td>
                    <td>{0[address_id]}</td>

                </tr>
            """
            print(row_pic.format(row))
        print("</tbody>")
        print("</table>")
    else:
        print("error")
    print(doc2)


