import {
    withStreamlitConnection
} from "streamlit-component-lib"

import StreamlitFlowComponent from "./StreamLitFlowComponent";



const StreamlitFlowApp = (props) => {

    return <>
        {props.args.component === 'streamlit_flow' && <StreamlitFlowComponent {...props} />}
    </>;
} 

export default withStreamlitConnection(StreamlitFlowApp);