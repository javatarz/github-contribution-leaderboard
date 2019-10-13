(() => {
  const URL = 'http://localhost:5000/data.json';
  const INTERVAL = 10000;

  const fetchLeaderBoard = () => {
    const xhr = new XMLHttpRequest();

    xhr.onload = function () {
      if (xhr.status >= 200 && xhr.status < 300) {
        createLeaderBoardTable(xhr);
      } else {
        console.log('The request failed!');
      }
    };

    xhr.open('GET', URL);
    xhr.send();
  };

  const createLeaderBoardTable = ({ response }) => {
    const tableBody = document.getElementsByTagName('tbody')[0];

    JSON.parse(response).forEach((row, index) => {
      if (tableBody.rows[index]) {
        tableBody.deleteRow(index);
      }

      const { avatar, user_name, score } = row;

      const tr = tableBody.insertRow(index);
      const cell1 = tr.insertCell(0);
      const cell2 = tr.insertCell(1);

      const avatarImage = document.createElement('img');
      avatarImage.setAttribute('src', avatar);
      avatarImage.setAttribute('alt', name);

      const avatarName = document.createElement('span');
      avatarName.innerText = user_name;

      cell1.appendChild(avatarImage);
      cell1.appendChild(avatarName);
      cell2.innerText = score;
    });
  };

  fetchLeaderBoard();
  setInterval(() => {
    fetchLeaderBoard();
  }, INTERVAL);
})();
