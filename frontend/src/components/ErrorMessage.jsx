import PropTypes from 'prop-types';

const ErrorMessage = ( { errorMessage } ) =>{
  return (
    <div className="w-full p-4 mb-4 mt-2 text-sm text-red-800 rounded-lg bg-red-500 dark:bg-gray-800 dark:text-red-400" role="alert">
      <span className="font-medium">Error!</span> {errorMessage}
    </div>
  )
}

ErrorMessage.propTypes = {
  errorMessage: PropTypes.string.isRequired,
};

export default ErrorMessage;

