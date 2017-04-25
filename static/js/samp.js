let Flat = React.createClass({

    getInitialState: function() {
        return {
            visible: false
        };
    },

    readMoreClick: function(e) {
        e.preventDefault();
        this.setState({visible: true});
    },

    /* Sample code for remote js calls.
    componentDidMount: function() {
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
    */

    render: function() {
        let author = this.props.data.url;
        let text = this.props.data.description;
        let bigText = this.props.data.owner.id;
        let visible = this.state.visible;

        return (
            <div className='container flat'>
                <div className="col-xs-2">
                    <span href="#" className="thumbnail">
                        <img src="/static/AQUILA.jpg" alt="Фото предложения" />
                    </span>
                </div>
                <div className="col-xs-5">
                    <p className='news_author'>{author}:</p>
                </div>
                <div className="col-xs-5">
                    <p className='news_text'>{text}</p>
                </div>
                <a href="#"
                    onClick={this.readMoreClick}
                    className={'btn btn-success btn-lg ' + (visible ? 'none': '')}>
                    Подробнее
                </a>
                <p className={'news_big-text ' + (visible ? '': 'none')}>{bigText}</p>
            </div>
        )
    }

});

let Flats = React.createClass({

  render: function() {
      let data = this.props.data;
      let flatsTemplate;

      if (data.length > 0) {
          flatsTemplate = data.map(function(item, index) {
              return (
                  <div className="col-xs-12" key={index}>
                      <Flat data={item} />
                  </div>
              )
          })
      } else {
        flatsTemplate = <p>К сожалению предложений нет</p>
      }

      return (
          <div>
              <div className='row'>
                  {flatsTemplate}
              </div>
              <p className='flats_count'>
                  <strong className={(data.length > 0 ? '':'none')}>Всего предложений: {data.length}</strong>
              </p>
          </div>
      );
  }

});

ReactDOM.render(
    <Flats data={flats}/>,
    document.getElementById('root')
);