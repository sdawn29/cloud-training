<html>
    <head>
        <title>Welcome to Log Reports</title>
    </head>
    <body>
        <h1>LOG REPORT</h1>
        <table border="1" bgcolor="green">
            % for ip, date, image, url in res:
            % if image == 'No Image':
            <tr bgcolor="yellow">
                <td>{{ ip }}</td>
                <td>{{ date }}</td>>
                <td bgcolor="red">{{ image }}</td>
                <td>{{ url }}</td>
            </tr>
            % else:
            <tr>
                <td>{{ ip }}</td>
                <td>{{ date }}</td>>
                <td>{{ image }}</td>
                <td>{{ url }}</td>
            </tr>
            % end
            % end
        </table>
    </body>
</html>