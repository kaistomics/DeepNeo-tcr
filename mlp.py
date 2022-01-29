import theano
import theano.tensor as T
import numpy
from theano.tensor.shared_randomstreams import RandomStreams

def relu(x):
    return T.maximum(0., x)

class HiddenLayer(object):
    def __init__(self, rng, 
		input, n_in, n_out, 
		activation=None, 
		W=None, b=None ,W_scale=None):
        self.input = input
	self.W_scale=W_scale

        if W is None:
	    W_values = numpy.asarray(
		self.W_scale * rng.standard_normal(size=(n_in, n_out) 
		), dtype=theano.config.floatX
	    )
            W = theano.shared(value=W_values, name='W', borrow=True)

        if b is None:
            b_values = numpy.zeros((n_out,), dtype=theano.config.floatX)
            b = theano.shared(value=b_values, name='b', borrow=True)

        self.W = W
        self.b = b
        self.params = [self.W, self.b]

        lin_output = T.dot(input, self.W) + self.b
	self.output = activation(lin_output)

def _dropout_from_layer( rng, input, p):
    srng = RandomStreams(rng.randint(2 **30))
    mask = srng.binomial(size=input.shape, n=1, p=1-p, dtype=theano.config.floatX)
    return input *mask

class DropoutHiddenLayer(HiddenLayer):
    def __init__(self, rng, 
		 input, n_in, n_out,
		 activation, dropout_rate, 
		 W=None, b=None, W_scale=None):
        super(DropoutHiddenLayer, self).__init__(rng=rng, 
		input=input, n_in=n_in, n_out=n_out,
                activation=activation, W=W, b=b, W_scale=W_scale)
        self.output = _dropout_from_layer(rng, self.output, p=dropout_rate)
