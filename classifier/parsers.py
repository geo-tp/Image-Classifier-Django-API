
class ClassifierParser:

    @staticmethod
    def format_predictions(predictions):
        formatted_prediction = ''

        for prediction in predictions:
            name = prediction[1].replace("_", " ").capitalize()
            rounded_percent = round(prediction[2]*100)
            final_percent =  rounded_percent if rounded_percent != 0 else 1
            formatted_prediction += "{} at {}%. ".format(name, final_percent)

        return formatted_prediction[0:-1]