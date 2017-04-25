const coreapi = window.coreapi;


let Flat = React.createClass({

    render: function() {
        let flat_type = this.props.data.flat_type;
        let rooms_quantity = this.props.data.rooms.length;
        let floor = this.props.data.floor;
        let description = this.props.data.description;

        let for_rent = this.props.data.for_rent;
        let per_room_basis = this.props.data.per_room_basis;
        let new_build = this.props.data.new_build;

        return (
            <div className="row tile_entity">
                <div className="col-xs-3">
                    <span href="#" className="thumbnail">
                        <img src="/static/AQUILA.jpg" alt="Фото предложения" />
                    </span>
                </div>
                <div className="col-xs-3">
                    <p><span className="text-info">Тип: </span>{flat_type == 'S' ? 'Студия':'Отдельная квартира'}</p>
                    <p><span className="text-info">Количество комнат: </span>{rooms_quantity}</p>
                    <p><span className="text-info">Этаж: </span>{floor}</p>
                    <p><span className="text-info">Описание: </span>{description}</p>
                </div>
                <div className="col-xs-3">
                    <p>
                        <span className="text-info">Сдаётся: </span>
                        {
                            for_rent ? <span className="text-success">Да</span>:<span className="text-danger">Нет</span>
                        }
                    </p>
                    <p>
                        <span className="text-info">По комнатам: </span>
                        {
                            per_room_basis ? <span className="text-success">Да</span>:<span className="text-danger">Нет</span>
                        }
                    </p>
                    <p>
                        <span className="text-info">Новостройка: </span>
                        {
                            new_build ? <span className="text-success">Да</span>:<span className="text-danger">Нет</span>
                        }
                    </p>
                </div>
                <GetOwner data={this.props.data.owner}/>
            </div>
        );

    }

});


let Room = React.createClass({

    render: function() {
        let room_type = this.props.data.room_type;
        let square = this.props.data.square;
        let description = this.props.data.description;

        let for_rent = this.props.data.for_rent;

        return (
            <div className="row tile_entity">
                <div className="col-xs-3">
                    <span href="#" className="thumbnail">
                        <img src="/static/AQUILA.jpg" alt="Фото предложения" />
                    </span>
                </div>
                <div className="col-xs-3">
                    <p><span className="text-info">Тип: </span>{room_type == 'L' ? 'Жилая':'Бытовая'}</p>
                    <p><span className="text-info">Площадь: </span>{square}</p>
                    <p><span className="text-info">Описание: </span>{description}</p>
                </div>
                <div className="col-xs-3">
                    <p>
                        <span className="text-info">Сдаётся: </span>
                        {
                            for_rent ? <span className="text-success">Да</span>:<span className="text-danger">Нет</span>
                        }
                    </p>
                </div>
                <GetOwner data={this.props.data.owner}/>
            </div>
        );

    }

});


let GetRoom = React.createClass({

    getInitialState: function() {
        return {
            data: null,
        };
    },

    componentDidMount: function() {
        let room_url = this.props.data;
        let client = new coreapi.Client();

        client.get(room_url)
            .then(function(result) {
                this.setState({data: result});
            }.bind(this))
            .catch(function (error) {
                console.log("ERROR: ", error);
            });
    },

    render: function() {

        if (this.state.data) {
            return <Room data={this.state.data} />;
        }

        return (
            <div className="row tile_entity">
                <div className="col-xs-12">
                    <span className="text-info">Loading...</span>
                </div>
            </div>
        );

    }

});


let PhysicalEntity = React.createClass({

    render: function() {
        let gender = this.props.data.gender;
        let birth_date = this.props.data.birth_date;
        let first_name = this.props.data.first_name;
        let second_name = this.props.data.second_name;
        let third_name = this.props.data.third_name;
        let phone_number = this.props.data.phone_number;
        let address_actual = this.props.data.address_actual;
        let address_registered = this.props.data.address_registered;
        let passport_series = this.props.data.passport_series;
        let passport_number = this.props.data.passport_number;
        let passport_issued_date = this.props.data.passport_issued_date;

        return (
            <div className="col-xs-3">
                <p><span className="text-info">Пол: </span>{gender}</p>
                <p><span className="text-info">Дата рождения: </span>{birth_date}</p>
                <p><span className="text-info">Имя: </span>{first_name}</p>
                <p><span className="text-info">Фамилия: </span>{second_name}</p>
                <p><span className="text-info">Отчество: </span>{third_name}</p>
                <p><span className="text-info">Номер телефона: </span>{phone_number}</p>
                <p><span className="text-info">Адрес проживания: </span>{address_actual}</p>
                <p><span className="text-info">Адрес регистрации: </span>{address_registered}</p>
                <p><span className="text-info">Серия паспорта: </span>{passport_series}</p>
                <p><span className="text-info">Номер паспорта: </span>{passport_number}</p>
                <p><span className="text-info">Дата выдачи паспорта: </span>{passport_issued_date}</p>
            </div>
        );

    }

});


let LegalEntity = React.createClass({

    render: function() {
        let company_name = this.props.data.company_name;
        let phone_number = this.props.data.phone_number;
        let address_actual = this.props.data.address_actual;
        let address_registered = this.props.data.address_registered;
        let inn = this.props.data.inn;

        return (
            <div className="col-xs-3">
                <p><span className="text-info">Название компании: </span>{company_name}</p>
                <p><span className="text-info">Номер телефона: </span>{phone_number}</p>
                <p><span className="text-info">Фактический адрес: </span>{address_actual}</p>
                <p><span className="text-info">Юридический адрес: </span>{address_registered}</p>
                <p><span className="text-info">ИНН: </span>{inn}</p>
            </div>
        );

    }

});


let GetOwner = React.createClass({

    getInitialState: function() {
        return {
            data: null,
        };
    },

    readMoreClick: function(event) {

        event.preventDefault();

        let owner_id = this.props.data.id;
        let owner_type = this.props.data.object_type == 'P' ? 'physical-entities' : 'legal-entities';
        let client = new coreapi.Client();

        client.get('http://localhost:8000/simulator/' + owner_type + '/' + owner_id)
            .then(function(result) {
                this.setState({data: result});
            }.bind(this))
            .catch(function (error) {
                console.log("ERROR: ", error);
            });
    },

    render: function() {

        if (this.state.data) {
            if (this.props.data.object_type == 'P') {
                return <PhysicalEntity data={this.state.data}/>;
            } else if (this.props.data.object_type == 'L') {
                return <LegalEntity data={this.state.data}/>;
            }
        }

        return (
            <div className="col-xs-3">
                <a href="#"
                    onClick={this.readMoreClick}
                    className="btn btn-success btn-s center">
                    Загрузить <br />
                    информацию <br />
                    о владельце
                </a>
            </div>
        );

    }

});


let FlatPageContainer = React.createClass({

    render: function() {
        let data = this.props.data;

        let rooms = data.rooms.map(function(item) {
            return (
                <GetRoom data={item} />
            )
        });

        return (
            <div className="container">
                <div className='row'>
                    <div className="col-xs-10">
                        <div className="col-xs-12">
                            <Flat data={data} />
                            <h2>Комнаты: </h2>
                            {rooms}
                        </div>
                    </div>
                </div>
            </div>
        );

    }

});


let root_element = document.getElementById('single_flat');

if (root_element) {
    ReactDOM.render(
        <FlatPageContainer data={single_flat}/>,
        root_element
    );
}
